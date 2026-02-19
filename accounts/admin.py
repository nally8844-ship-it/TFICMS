from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Customize admin site
admin.site.site_header = "🏥 TFICMS Admin Panel"
admin.site.site_title = "TFICMS Admin"
admin.site.index_title = "Welcome to TFICMS Management System"

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'department', 'is_staff', 'is_superuser')
    list_filter = ('department', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'phone')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Department', {'fields': ('department',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'phone', 'department', 'is_staff', 'is_superuser'),
        }),
    )