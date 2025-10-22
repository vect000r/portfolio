from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings

import logging

from rest_framework.response import Response

from .models import Education, Project
from .serializers import (
    EducationSerializer,
    ProjectSerializer,
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


@api_view(['POST'])
def contact(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    try:
        subject = f"Portfolio Contact: {name}"
        message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Message: {message}\n"
        )
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, recipient_list)

    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")


    return Response(
        {"status": "success", "message": "Your message has been sent"},
        status=status.HTTP_201_CREATED,
    )