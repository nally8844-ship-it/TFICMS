from rest_framework.routers import DefaultRouter
from .views import BillingPackageViewSet, InvoiceViewSet, PaymentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'packages', BillingPackageViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]