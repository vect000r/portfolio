from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EducationViewSet,
    ProjectViewSet,
    SkillViewSet,
)

router = DefaultRouter()
router.register('education', EducationViewSet, basename='education')
router.register('project', ProjectViewSet, basename='project')
router.register('skill', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]
