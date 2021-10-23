from django.db import models

# Create your models here.
class Photo(models.Model):
    username = models.IntegerField()
    photo_captured = models.TextField()
    photo_edited = models.TextField()

class Emoji(models.Model):
    emoji = models.TextField()
    emoji_id = models.TextField()

class Frame(models.Model):
    frame = models.TextField()
    frame_id = models.TextField()
