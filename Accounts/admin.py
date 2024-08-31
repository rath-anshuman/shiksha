from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

class UserAccountAdmin(UserAdmin):
    model = UserAccount
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(UserAccount, UserAccountAdmin)
