from rest_framework.routers import DefaultRouter
from .views import StaffProfileViewSet, AttendanceViewSet, PayrollViewSet, LeaveApplicationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'staff-profiles', StaffProfileViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'leave', LeaveApplicationViewSet)

urlpatterns = [ path('api/', include(router.urls)), ]