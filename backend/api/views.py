from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.throttling import UserRateThrottle
from django.shortcuts import render
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

def gloria_view(request):
    """
    Renders the flowers for the gloria view
    """
    return render(request, 'gloria.html')