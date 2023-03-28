from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    link = models.URLField(blank=True)

    class Meta:
        app_label = 'api'


class CV(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='cv')

    class Meta:
        app_label = 'api'

class About(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    git_hub = models.URLField()
    linked_in = models.URLField()
    intro = models.TextField()

    class Meta:
        app_label = 'api'
