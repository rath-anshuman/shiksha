from django.contrib import admin

# Register your models here.
from .models import Routine,classes


admin.site.register(Routine)
admin.site.register(classes)
