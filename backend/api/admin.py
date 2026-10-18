from django.contrib import admin
from .models import Education, Experience, Project, Skill

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin interface for Education model."""

    list_display = ['school', 'degree', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    ordering = ['order', '-start_date']
    search_fields = ['school', 'degree', 'field_of_study']
    list_filter = ['start_date']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Project model."""

    list_display = ['title', 'short_description', 'order', 'created_at']
    list_editable = ['order']
    ordering = ['order', '-created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order",)
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    ordering = ('order', '-start_date')
    search_fields = ('company', 'role', 'description')
    list_filter = ('start_date', 'end_date')