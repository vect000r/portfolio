from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)