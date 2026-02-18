from django.contrib import admin
from .models import IVFCycle, StimulationDay, EggRetrieval, EmbryoTransfer

@admin.register(IVFCycle)
class IVFCycleAdmin(admin.ModelAdmin):
    list_display = ('id','couple','protocol','status','start_date','created_at')

@admin.register(StimulationDay)
class StimulationDayAdmin(admin.ModelAdmin):
    list_display = ('id','ivf_cycle','day_number','date','estradiol','lh','progesterone','dominant_follicles')

@admin.register(EggRetrieval)
class EggRetrievalAdmin(admin.ModelAdmin):
    list_display = ('id','ivf_cycle','date','eggs_collected','matured_eggs')

@admin.register(EmbryoTransfer)
class EmbryoTransferAdmin(admin.ModelAdmin):
    list_display = ('id','ivf_cycle','date','embryos_transferred','quality','outcome')