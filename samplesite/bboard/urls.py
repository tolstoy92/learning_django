from django.urls import path

from .views import index, demo


urlpatterns = [
    path('', index),
    path('demo/', demo)
]
