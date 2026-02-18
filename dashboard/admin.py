from django.contrib import admin
from .models import DashboardSetting


@admin.register(DashboardSetting)
class DashboardSettingAdmin(admin.ModelAdmin):
    list_display = ('theme_color', 'show_charts', 'items_per_page')