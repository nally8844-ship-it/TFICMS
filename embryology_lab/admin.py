from django.contrib import admin
from .models import Oocyte, Fertilization, Embryo

@admin.register(Oocyte)
class OocyteAdmin(admin.ModelAdmin):
    list_display=['id','ivf_cycle','retrieval_date','number_retrieved','mature','witness','barcode']
    search_fields=['barcode']

@admin.register(Fertilization)
class FertilizationAdmin(admin.ModelAdmin):
    list_display=['id','oocyte','date','method','fertilized','normal','abnormal']

@admin.register(Embryo)
class EmbryoAdmin(admin.ModelAdmin):
    list_display=['id','ivf_cycle','day','grade','biopsy_done','cryo_stored','witness','barcode']
    search_fields=['barcode']