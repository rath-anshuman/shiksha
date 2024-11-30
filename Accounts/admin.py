from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'regno', 'section', 'email', 'is_active', 'is_staff')
    list_filter = ('section', 'is_active', 'is_staff')
    ordering = ('regno',)
