from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    head = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Permission(models.Model):
    PERMISSION_CHOICES = [
        ('view_patients', 'View Patients'),
        ('add_patients', 'Add Patients'),
        ('edit_patients', 'Edit Patients'),
        ('delete_patients', 'Delete Patients'),
        ('view_appointments', 'View Appointments'),
        ('add_appointments', 'Add Appointments'),
        ('edit_appointments', 'Edit Appointments'),
        ('delete_appointments', 'Delete Appointments'),
        ('view_reports', 'View Reports'),
        ('add_reports', 'Add Reports'),
        ('view_finance', 'View Finance'),
        ('add_finance', 'Add Finance'),
        ('edit_finance', 'Edit Finance'),
        ('view_staff', 'View Staff'),
        ('add_staff', 'Add Staff'),
        ('delete_staff', 'Delete Staff'),
        ('view_samples', 'View Samples'),
        ('add_samples', 'Add Samples'),
        ('view_lab_results', 'View Lab Results'),
        ('add_lab_results', 'Add Lab Results'),
        ('view_patients_history', 'View Patient History'),
        ('manage_schedule', 'Manage Schedule'),
    ]
    
    permission = models.CharField(max_length=100, choices=PERMISSION_CHOICES, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.get_permission_display()

class DepartmentPermission(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('department', 'permission')
    
    def __str__(self):
        return f"{self.department.name} - {self.permission.permission}"

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Active', choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    doctor = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient.name} - {self.department}"

class Staff(models.Model):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Technician', 'Technician'),
        ('Administrator', 'Administrator'),
        ('Receptionist', 'Receptionist'),
        ('Lab Technician', 'Lab Technician'),
        ('Embryologist', 'Embryologist'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    joining_date = models.DateField()
    status = models.CharField(max_length=20, default='Active', choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Finance(models.Model):
    TRANSACTION_TYPE = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

class Sample(models.Model):
    SAMPLE_TYPE_CHOICES = [
        ('Sperm', 'Sperm'),
        ('Egg', 'Egg'),
        ('Embryo', 'Embryo'),
        ('Tissue', 'Tissue'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sample_type = models.CharField(max_length=50, choices=SAMPLE_TYPE_CHOICES)
    collection_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Processed', 'Processed'), ('Archived', 'Archived')])
    
    def __str__(self):
        return f"{self.sample_type} - {self.patient.name}"

class LabResult(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.TextField()
    date_tested = models.DateTimeField(auto_now_add=True)
    normal_range = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    
    def __str__(self):
        return f"{self.test_name} - {self.sample.patient.name}"

class DepartmentReport(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    total_appointments = models.IntegerField(default=0)
    completed_appointments = models.IntegerField(default=0)
    total_patients = models.IntegerField(default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.department.name} - Report"
