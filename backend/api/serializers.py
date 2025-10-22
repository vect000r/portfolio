from rest_framework import serializers
from api.models import Education, Project, Resume


class EducationSerializer(serializers.ModelSerializer):
    """Serializer for Education model."""

    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id',)


class ResumeSerializer(serializers.ModelSerializer):
    """Serializer for Resume model."""

    class Meta:
        model = Resume
        fields = ['id', 'title', 'file', 'uploaded_at']
        read_only_fields = ('id', 'uploaded_at')