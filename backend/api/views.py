from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Education, Experience, Project, Skill
from .serializers import (
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
)


class PublicReadAdminWriteViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = (
            [AllowAny] if self.action in ['list', 'retrieve'] else [IsAdminUser]
        )
        return [permission() for permission in permission_classes]


class EducationViewSet(PublicReadAdminWriteViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ProjectViewSet(PublicReadAdminWriteViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillViewSet(PublicReadAdminWriteViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(PublicReadAdminWriteViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
