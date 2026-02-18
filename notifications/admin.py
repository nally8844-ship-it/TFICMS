from django.contrib import admin
from .models import NotificationTemplate, NotificationLog

@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ['id','name','type','subject']

@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ['id','recipient','notification_type','subject','sent_at','status']