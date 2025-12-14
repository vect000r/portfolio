from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EducationViewSet,
    ProjectViewSet,
    SkillViewSet,
    gloria_view
)

router = DefaultRouter()
router.register('education', EducationViewSet, basename='education')
router.register('project', ProjectViewSet, basename='project')
router.register('skill', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
    path('gloria/', gloria_view, name='gloria')
]
