from django.db import models

# Create your models here.
class movieUping(models.Model):
    video = models.URLField()
    movie_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    release_year = models.CharField(max_length=20)
    video_id = models.CharField(max_length=20)