from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    poster = models.URLField()
    description = models.TextField(blank=True)

    # ❌ REMOVE this (not needed anymore)
    # liked = models.BooleanField(default=False)

    # ❤️ Like system (user-based)
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_movies',
        blank=True
    )

    # 📌 Watchlist system (NEW - REQUIRED)
    watchlisted_by = models.ManyToManyField(
        User,
        related_name='watchlist',
        blank=True
    )

    def __str__(self):
        return self.title