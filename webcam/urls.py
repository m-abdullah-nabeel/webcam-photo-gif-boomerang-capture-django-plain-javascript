from django.urls import path

from . import views

urlpatterns = [
    path('camera/', views.capture, name='capture'),
    path('editor/<id>', views.editor, name='editor'),
    path('show/<id>', views.show, name='show'),
    path('mypics/', views.ListOnes, name='ListOnes'),
    path('add-frames/', views.add_frames, name='add_frames'),
    path('add-images/', views.add_images, name='add_images'),
]
