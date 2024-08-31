from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from tadmin import urls as turls
from Accounts import urls as uurls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(turls)),
    path('users/',include(uurls)),
]

urlpatterns+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)