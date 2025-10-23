from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.http import require_http_methods
import json

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


@csrf_exempt
@require_http_methods(["POST"])
def contact(request):
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message_body = data.get('message', '').strip()

        if not name or not email or not message_body:
            return JsonResponse(
                {"error": "All fields are required"},
                status=400
            )

        # Send email
        from django.core.mail import send_mail
        from django.conf import settings

        subject = f"Portfolio Contact from {name}"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )

        return JsonResponse(
            {"message": "Your message has been sent"},
            status=200
        )

    except Exception as e:
        return JsonResponse(
            {"error": "Failed to send message"},
            status=500
        )