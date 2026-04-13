from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'is_staff']
    

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role', 'phone', 'address')}),
    )
    

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('role', 'phone', 'address')}),
    )