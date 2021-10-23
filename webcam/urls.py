from django.urls import path

from . import views

urlpatterns = [
    path('camera/', views.capture, name='capture'),
    path('editor/<id>', views.editor, name='editor'),
    path('show/<id>', views.show, name='show'),
    path('mypics/', views.ListOnes, name='ListOnes'),
]
