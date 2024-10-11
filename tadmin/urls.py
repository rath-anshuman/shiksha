from django.urls import path,include

from .views import routine,routinedtl
from .views import routine,routinedtl,classstate,routine_sec,routine_sec_day

urlpatterns = [
    path('routine/',routine),
    path('routine/<int:pk>',routinedtl),
    path('routine/<str:sec>',routine_sec),
    path('routine/<str:sec>/<str:day>',routine_sec_day),
    path('class/',classstate),
]
