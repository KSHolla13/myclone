from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Streams(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

class Movies(models.Model):
    name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=100)
    stream = models.ForeignKey(Streams, on_delete=models.CASCADE, related_name="stream")
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    no_of_rating = models.FloatField(default=0)

