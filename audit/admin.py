from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditAdmin(admin.ModelAdmin):
    list_display=['id','timestamp','action','model','object_id','user','ip_addr']
    search_fields=['model','user__username','action']