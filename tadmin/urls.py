from django.urls import path,include

from .views import routine,routinedtl
from .views import routine,routinedtl,classstate

urlpatterns = [
    path('routine/',routine),
    path('routine/<int:pk>',routinedtl),
    path('class/',classstate),
]
