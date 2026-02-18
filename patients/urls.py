from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, CoupleProfileViewSet, PatientDocumentViewSet, ConsentFormViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'couples', CoupleProfileViewSet)
router.register(r'patient-documents', PatientDocumentViewSet)
router.register(r'consent-forms', ConsentFormViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]