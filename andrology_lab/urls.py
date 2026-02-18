from rest_framework.routers import DefaultRouter
from .views import SemenAnalysisViewSet, SpermPreparationViewSet, SpermFreezingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'semen', SemenAnalysisViewSet)
router.register(r'sperm-prep', SpermPreparationViewSet)
router.register(r'sperm-freeze', SpermFreezingViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]