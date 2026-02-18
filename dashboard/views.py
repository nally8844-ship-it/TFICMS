import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from patients.models import Patient
from billing.models import Invoice, Payment
from pharmacy.models import Drug
from hr_payroll.models import StaffProfile


@login_required
def admin_dashboard(request):
    """
    Dashboard view showing clinic statistics and recent activities
    """
    
    # Get today's date
    today = datetime.date.today()
    
    try:
        # Calculate statistics
        total_patients = Patient.objects.count()
        today_appointments = Appointment.objects.filter(
            scheduled_time__date=today
        ).count()
        
        # Get invoices count - Invoice model available fields
        try:
            pending_invoices = Invoice.objects.count()
        except:
            pending_invoices = 0
        
        # Get payments count - Payment has: amount, date, id, invoice, invoice_id, mode, notes
        try:
            recent_payments_list = Payment.objects.order_by('-date')[:5]
            pending_payments = Payment.objects.count()
        except:
            recent_payments_list = []
            pending_payments = 0
        
        # Get staff count
        try:
            total_staff = StaffProfile.objects.count()
        except:
            total_staff = 0
        
        # Get available drugs
        try:
            available_drugs = Drug.objects.filter(quantity__gt=0).count()
        except:
            available_drugs = 0
        
        # Get recent appointments (last 5)
        try:
            recent_appointments = Appointment.objects.order_by('-scheduled_time')[:5]
        except:
            recent_appointments = []
        
        # Get recent invoices (last 5)
        try:
            recent_invoices = Invoice.objects.order_by('-id')[:5]
        except:
            recent_invoices = []
        
    except Exception as e:
        # If there are any errors, provide default values
        total_patients = 0
        today_appointments = 0
        pending_invoices = 0
        pending_payments = 0
        total_staff = 0
        available_drugs = 0
        recent_appointments = []
        recent_invoices = []
        recent_payments_list = []
    
    context = {
        'total_patients': total_patients,
        'today_appointments': today_appointments,
        'pending_invoices': pending_invoices,
        'pending_payments': pending_payments,
        'total_staff': total_staff,
        'available_drugs': available_drugs,
        'recent_appointments': recent_appointments,
        'recent_invoices': recent_invoices,
        'recent_payments': recent_payments_list,
    }
    
    return render(request, 'home.html', context)