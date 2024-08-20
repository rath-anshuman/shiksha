from django.urls import path,include

from .views import routine,routinedtl,list_routine

urlpatterns = [
    path('routine/',routine),
    path('routine/l/',list_routine),
    path('routine/<int:pk>',routinedtl),
]
