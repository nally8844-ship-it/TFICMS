from rest_framework.routers import DefaultRouter
from .views import CryotankViewSet, CryoStorageRecordViewSet, DonorViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tanks', CryotankViewSet)
router.register(r'storage', CryoStorageRecordViewSet)
router.register(r'donors', DonorViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]