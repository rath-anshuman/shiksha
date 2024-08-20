from django.urls import path,include

from .views import routine,routinedtl

urlpatterns = [
    path('routine/',routine),
    path('routine/<int:pk>',routinedtl),
]
