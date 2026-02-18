from rest_framework.routers import DefaultRouter
from .views import DrugViewSet, PrescriptionDispensingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'drugs', DrugViewSet)
router.register(r'dispensings', PrescriptionDispensingViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]