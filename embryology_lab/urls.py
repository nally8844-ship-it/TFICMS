from rest_framework.routers import DefaultRouter
from .views import OocyteViewSet, FertilizationViewSet, EmbryoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'oocytes', OocyteViewSet)
router.register(r'fertilizations', FertilizationViewSet)
router.register(r'embryos', EmbryoViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]