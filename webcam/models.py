from django.db import models

# Create your models here.
class Photo(models.Model):
    photo_captured = models.TextField()
    photo_edited = models.TextField()

class Emoji(models.Model):
    emoji = models.TextField()

class Frame(models.Model):
    frame = models.TextField(default=1)
