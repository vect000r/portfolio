from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    description = models.TextField()
    education_id = models.IntegerField()

    class Meta:
        ordering = ['education_id']
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.school


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    project_id = models.IntegerField()

    class Meta:
        ordering = ['project_id']

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return self.title