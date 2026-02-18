from django.db import models
from accounts.models import User

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hire_date = models.DateField()
    position = models.CharField(max_length=120)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    phone = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.position})"

class Attendance(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    notes = models.CharField(max_length=128, blank=True)

class Payroll(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    month = models.CharField(max_length=7) # format: YYYY-MM
    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bonuses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_on = models.DateField(null=True, blank=True)

class LeaveApplication(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    reason = models.CharField(max_length=256)
    status = models.CharField(max_length=16, choices=(('pending','Pending'),('approved','Approved'),('rejected','Rejected')), default='pending')
    applied_on = models.DateField(auto_now_add=True)
    acted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='leave_approvals')
    action_date = models.DateField(null=True, blank=True)