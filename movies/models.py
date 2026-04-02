from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    poster = models.URLField()
    liked = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    liked_by = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return self.title