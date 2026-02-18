from django.contrib import admin
from .models import Cryotank, CryoStorageRecord, Donor

@admin.register(Cryotank)
class CryotankAdmin(admin.ModelAdmin):
    list_display = ['id','name','capacity','location','temperature']

@admin.register(CryoStorageRecord)
class CryoStorageAdmin(admin.ModelAdmin):
    list_display = ['id','patient','specimen_type','tank','canister','goblet','straw','barcode','witness','is_active']

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['id','code','name','donor_type','active']