from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("preview_voice/", views.preview_voice, name="preview_voice"),
]
