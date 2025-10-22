from rest_framework import serializers
from api.models import Education, Project

class EducationSerializer(serializers.ModelSerializer):
    """Serializer for Education model."""
    years_display = serializers.CharField(source='get_years_display', read_only=True)

    class Meta:
        model = Education
        fields = [
            'id',
            'school',
            'degree',
            'field_of_study',
            'start_date',
            'end_date',
            'years_display',
            'description',
            'location',
            'gpa',
            'order'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'short_description',
            'image',
            'live_url',
            'github_url',
            'order',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate(self, data):
        """Ensure at least one URL is provided"""
        if not data.get('url') and not data.get('github_url'):
            raise serializers.ValidationError(
                "At least one of 'url' or 'github_url' must be provided"
            )
        return data