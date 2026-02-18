from rest_framework import viewsets, permissions
from .models import StaffProfile, Attendance, Payroll, LeaveApplication
from .serializers import StaffProfileSerializer, AttendanceSerializer, PayrollSerializer, LeaveApplicationSerializer

class StaffProfileViewSet(viewsets.ModelViewSet):
    queryset = StaffProfile.objects.all().select_related('user')
    serializer_class = StaffProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().select_related('staff')
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all().select_related('staff')
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all().select_related('staff')
    serializer_class = LeaveApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]