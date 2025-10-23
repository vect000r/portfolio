from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.throttling import UserRateThrottle

import logging

from rest_framework.response import Response

from .models import Education, Project, Skill
from .serializers import (
    EducationSerializer,
    ProjectSerializer,
    SkillSerializer,
)

logger = logging.getLogger(__name__)

class EducationViewSet(viewsets.ModelViewSet):
    """API endpoint for Education objects."""
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_permissions(self):
        """
        Allow anyone to read, but only admins can write.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint for Project objects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        """
        Allow anyone to read, but only admins can write.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class SkillViewSet(viewsets.ModelViewSet):
    """API endpoint for Skill objects."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactThrottle(UserRateThrottle):
    scope = 'contact'

@api_view(['POST'])
@permission_classes([])
@throttle_classes([ContactThrottle])
def contact(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message_body = request.data.get('message')

    if not name or not email or not message_body:
        return Response(
            {"status": "error", "message": "All fields are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        subject = f"Portfolio Contact: {name}"
        message_text = f"Name: {name}\nEmail: {email}\nMessage: {message_body}\n"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message_text, from_email, recipient_list)

    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")
        return Response(
            {"status": "error", "message": "Failed to send message"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response(
        {"status": "success", "message": "Your message has been sent"},
        status=status.HTTP_201_CREATED
    )

contact = csrf_exempt(contact)