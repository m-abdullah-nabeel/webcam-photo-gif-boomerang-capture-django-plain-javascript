from django.contrib import admin

from .models import Frame, Photo, Emoji

admin.site.register(Photo)
admin.site.register(Emoji)
admin.site.register(Frame)
