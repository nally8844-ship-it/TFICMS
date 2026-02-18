from django.contrib import admin
from .models import StaffProfile, Attendance, Payroll, LeaveApplication

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','position','hire_date','salary','is_active']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id','staff','date','check_in','check_out']

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['id','staff','month','base_salary','deductions','bonuses','net_pay','paid']

@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display=['id','staff','date_from','date_to','reason','status','applied_on']