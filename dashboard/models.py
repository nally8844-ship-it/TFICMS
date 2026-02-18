from django.db import models

# Dashboard app models (if needed in the future)
class DashboardSetting(models.Model):
    """Store dashboard customization settings"""
    theme_color = models.CharField(max_length=7, default='#667eea')
    show_charts = models.BooleanField(default=True)
    items_per_page = models.IntegerField(default=10)
    
    class Meta:
        verbose_name_plural = "Dashboard Settings"
    
    def __str__(self):
        return "Dashboard Settings"