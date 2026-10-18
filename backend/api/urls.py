from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EducationViewSet, ExperienceViewSet, ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register('education', EducationViewSet, basename='education')
router.register('project', ProjectViewSet, basename='project')
router.register('skill', SkillViewSet, basename='skill')
router.register('experience', ExperienceViewSet, basename='experience')

urlpatterns = [
    path('', include(router.urls)),
]
