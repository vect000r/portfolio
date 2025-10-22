from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Education, Project
from .serializers import (
    EducationSerializer,
    ProjectSerializer,
)

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





