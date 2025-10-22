from django.db import models


class Education(models.Model):
    """
    Represents an education stage.
    """

    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text="Leave blank if currently enrolled"
    )
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    gpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers first)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} at {self.school}"

    @property
    def years_display(self):
        """Returns formatted year range"""
        start = self.start_date.year
        end = self.end_date.year if self.end_date else 'Present'
        return f"{start} - {end}"


class Project(models.Model):
    """
    Represents a portfolio project.
    """

    title = models.CharField(max_length=200)
    short_description = models.CharField(
        max_length=200,
        help_text="Brief summary for cards"
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/%Y/%m/',
        blank=True,
        null=True
    )
    live_url = models.URLField(
        blank=True,
        help_text="Live project URL"
    )
    github_url = models.URLField(
        blank=True,
        help_text="GitHub repository"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers first)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    Represents a skill that I posses
    """
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('frontend', 'Frontend'),
            ('backend', 'Backend'),
            ('tools', 'Tools & Other'),
            ('soft', 'Soft skills'),
        ]
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

