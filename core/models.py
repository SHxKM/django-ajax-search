from django.db import models
from django.utils import timezone

# Create your models here.


class MusicRelease(models.Model):
    title = models.CharField(max_length=560)
    release_date = models.DateField(blank=True, null=True)  # some releases don't have release-dates

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("release_date",)

    @property
    def is_released(self):
        return self.release_date < timezone.now().date()


class Artist(models.Model):
    music_releases = models.ManyToManyField(MusicRelease, blank=True)
    name = models.CharField(max_length=560)

    def __str__(self):
        return f"{self.name} (release count: {self.music_releases.count()})"
