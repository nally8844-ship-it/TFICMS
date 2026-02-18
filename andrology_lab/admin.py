from django.contrib import admin
from .models import SemenAnalysis, SpermPreparation, SpermFreezing

@admin.register(SemenAnalysis)
class SemenAnalysisAdmin(admin.ModelAdmin):
    list_display=['id','patient','date','volume_ml','concentration_million_per_ml','motility_percent','morphology_percent','analyst']
    search_fields=['patient__first_name','patient__last_name']

@admin.register(SpermPreparation)
class SpermPrepAdmin(admin.ModelAdmin):
    list_display=['id','semen','preparation_type','date','processed_by']
    search_fields=['semen__patient__first_name']

@admin.register(SpermFreezing)
class SpermFreezingAdmin(admin.ModelAdmin):
    list_display=['id','patient','date','straws_frozen','barcode','thawed','witness']
    search_fields=['barcode','patient__first_name']