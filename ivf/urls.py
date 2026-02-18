from rest_framework.routers import DefaultRouter
from .views import IVFCycleViewSet, StimulationDayViewSet, EggRetrievalViewSet, EmbryoTransferViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'ivf-cycles', IVFCycleViewSet)
router.register(r'stimulation-days', StimulationDayViewSet)
router.register(r'egg-retrievals', EggRetrievalViewSet)
router.register(r'embryo-transfers', EmbryoTransferViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]