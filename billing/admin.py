from django.contrib import admin
from .models import BillingPackage, Invoice, Payment

@admin.register(BillingPackage)
class BillingPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['id','patient','amount','outstanding_balance','status','issue_date','due_date']
    list_filter=['status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','invoice','amount','date','mode']