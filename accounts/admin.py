from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

# admin.site.register(CustomUser)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha Info", {"fields": ("age", "phone")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("age", "phone")}),
    )
    list_display = UserAdmin.list_display + ("age", "phone")
    ordering = ("username",)