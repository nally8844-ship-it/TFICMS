from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.db import models
from apps.core.models import Patient, Appointment, Staff, Finance, Department, Sample, LabResult
import json

# All API functions (login, logout, patients, staff, etc.)
@csrf_exempt
def login_api(request):
    if request.method != 'POST':
        return JsonResponse({'success': False}, status=405)
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password = data.get('password', '')
        if not username or not password:
            return JsonResponse({'success': False, 'message': 'Missing credentials'}, status=400)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'success': True, 'username': user.username, 'email': user.email, 'is_staff': user.is_staff, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
def logout_api(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logged out'})

@csrf_exempt
def user_info(request):
    if request.user.is_authenticated:
        return JsonResponse({'success': True, 'username': request.user.username, 'email': request.user.email, 'is_staff': request.user.is_staff})
    return JsonResponse({'success': False, 'message': 'Not authenticated'}, status=401)

@csrf_exempt
def users_api(request):
    if request.method == 'GET':
        try:
            users = User.objects.all().values('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined')
            return JsonResponse({'success': True, 'users': list(users)})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            email = data.get('email', '').strip()
            password = data.get('password', '')
            if not username or not email or not password:
                return JsonResponse({'success': False, 'message': 'Missing fields'}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'}, status=400)
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'success': True, 'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def user_detail_api(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'success': True, 'message': 'User deleted'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def patients_api(request):
    if request.method == 'GET':
        try:
            patients = Patient.objects.all().values('id', 'name', 'email', 'phone', 'age', 'gender', 'status', 'registration_date')
            return JsonResponse({'success': True, 'patients': list(patients)})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.create(name=data.get('name'), email=data.get('email'), phone=data.get('phone'), age=data.get('age'), gender=data.get('gender'), address=data.get('address'), status='Active')
            return JsonResponse({'success': True, 'message': 'Patient created successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def patient_detail_api(request, patient_id):
    if request.method == 'GET':
        try:
            patient = Patient.objects.get(id=patient_id)
            return JsonResponse({'success': True, 'patient': {'id': patient.id, 'name': patient.name, 'email': patient.email, 'phone': patient.phone, 'age': patient.age, 'gender': patient.gender, 'address': patient.address, 'status': patient.status, 'registration_date': patient.registration_date.isoformat()}})
        except Patient.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Patient not found'}, status=404)
    elif request.method == 'DELETE':
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            return JsonResponse({'success': True, 'message': 'Patient deleted'})
        except Patient.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Patient not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def appointments_api(request):
    if request.method == 'GET':
        try:
            appointments = list(Appointment.objects.select_related('patient', 'department').values('id', 'patient__name', 'department__name', 'doctor', 'appointment_date', 'status'))
            result = [{'id': apt['id'], 'patient_name': apt['patient__name'], 'department': apt['department__name'], 'doctor': apt['doctor'], 'appointment_date': apt['appointment_date'].isoformat(), 'status': apt['status']} for apt in appointments]
            return JsonResponse({'success': True, 'appointments': result})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            appointment = Appointment.objects.create(patient_id=data.get('patient_id'), department_id=data.get('department_id'), doctor=data.get('doctor'), appointment_date=data.get('appointment_date'), notes=data.get('notes', ''), status='Pending')
            return JsonResponse({'success': True, 'message': 'Appointment created successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def appointment_detail_api(request, appointment_id):
    if request.method == 'DELETE':
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return JsonResponse({'success': True, 'message': 'Appointment deleted'})
        except Appointment.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Appointment not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def staff_api(request):
    if request.method == 'GET':
        try:
            staff_members = list(Staff.objects.all().values('id', 'name', 'email', 'phone', 'role', 'department__name', 'joining_date', 'status'))
            return JsonResponse({'success': True, 'staff': staff_members})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            staff = Staff.objects.create(name=data.get('name'), email=data.get('email'), phone=data.get('phone'), role=data.get('role'), department_id=data.get('department_id'), joining_date=data.get('joining_date'), status='Active')
            return JsonResponse({'success': True, 'message': 'Staff member added successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def staff_detail_api(request, staff_id):
    if request.method == 'DELETE':
        try:
            staff = Staff.objects.get(id=staff_id)
            staff.delete()
            return JsonResponse({'success': True, 'message': 'Staff member deleted'})
        except Staff.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Staff not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def finance_api(request):
    if request.method == 'GET':
        try:
            department_id = request.GET.get('department_id')
            query = Finance.objects.select_related('patient', 'department')
            if department_id:
                query = query.filter(department_id=department_id)
            finance = list(query.values('id', 'transaction_type', 'amount', 'description', 'patient__name', 'department__name', 'transaction_date', 'reference_number'))
            result = [{'id': trans['id'], 'transaction_type': trans['transaction_type'], 'amount': str(trans['amount']), 'description': trans['description'], 'patient_name': trans['patient__name'] or 'N/A', 'department_name': trans['department__name'] or 'General', 'transaction_date': trans['transaction_date'].isoformat(), 'reference_number': trans['reference_number']} for trans in finance]
            return JsonResponse({'success': True, 'finance': result})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            finance = Finance.objects.create(transaction_type=data.get('transaction_type'), amount=data.get('amount'), description=data.get('description'), patient_id=data.get('patient_id') or None, department_id=data.get('department_id') or None, reference_number=data.get('reference_number'))
            return JsonResponse({'success': True, 'message': 'Transaction recorded successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def finance_detail_api(request, finance_id):
    if request.method == 'DELETE':
        try:
            finance = Finance.objects.get(id=finance_id)
            finance.delete()
            return JsonResponse({'success': True, 'message': 'Transaction deleted'})
        except Finance.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Transaction not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def samples_api(request):
    if request.method == 'GET':
        try:
            department_id = request.GET.get('department_id')
            query = Sample.objects.select_related('patient', 'department')
            if department_id:
                query = query.filter(department_id=department_id)
            samples = list(query.values('id', 'sample_type', 'patient__name', 'collection_date', 'department__name', 'status', 'notes'))
            return JsonResponse({'success': True, 'samples': samples})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            sample = Sample.objects.create(patient_id=data.get('patient_id'), sample_type=data.get('sample_type'), collection_date=data.get('collection_date'), department_id=data.get('department_id'), notes=data.get('notes', ''), status='Pending')
            return JsonResponse({'success': True, 'message': 'Sample recorded successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def sample_detail_api(request, sample_id):
    if request.method == 'DELETE':
        try:
            sample = Sample.objects.get(id=sample_id)
            sample.delete()
            return JsonResponse({'success': True, 'message': 'Sample deleted'})
        except Sample.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Sample not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def lab_results_api(request):
    if request.method == 'GET':
        try:
            sample_id = request.GET.get('sample_id')
            query = LabResult.objects.select_related('sample', 'sample__patient')
            if sample_id:
                query = query.filter(sample_id=sample_id)
            results = list(query.values('id', 'sample__id', 'test_name', 'result', 'date_tested', 'normal_range', 'status', 'sample__patient__name'))
            return JsonResponse({'success': True, 'results': results})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            lab_result = LabResult.objects.create(sample_id=data.get('sample_id'), test_name=data.get('test_name'), result=data.get('result'), normal_range=data.get('normal_range', ''), status='Completed')
            return JsonResponse({'success': True, 'message': 'Lab result recorded successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def lab_result_detail_api(request, result_id):
    if request.method == 'DELETE':
        try:
            lab_result = LabResult.objects.get(id=result_id)
            lab_result.delete()
            return JsonResponse({'success': True, 'message': 'Lab result deleted'})
        except LabResult.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Lab result not found'}, status=404)
    return JsonResponse({'success': False}, status=405)

@csrf_exempt
def department_stats_api(request):
    try:
        department_id = request.GET.get('department_id')
        if not department_id:
            return JsonResponse({'success': False, 'message': 'Department ID required'}, status=400)
        dept = Department.objects.get(id=department_id)
        total_appointments = Appointment.objects.filter(department_id=department_id).count()
        completed_appointments = Appointment.objects.filter(department_id=department_id, status='Completed').count()
        patient_ids = Appointment.objects.filter(department_id=department_id).values_list('patient_id', flat=True).distinct()
        total_patients = len(patient_ids)
        income = Finance.objects.filter(department_id=department_id, transaction_type='Income').aggregate(total=models.Sum('amount'))['total'] or 0
        expense = Finance.objects.filter(department_id=department_id, transaction_type='Expense').aggregate(total=models.Sum('amount'))['total'] or 0
        total_samples = Sample.objects.filter(department_id=department_id).count()
        total_staff = Staff.objects.filter(department_id=department_id).count()
        return JsonResponse({'success': True, 'department': dept.name, 'total_appointments': total_appointments, 'completed_appointments': completed_appointments, 'total_patients': total_patients, 'total_income': float(income), 'total_expense': float(expense), 'net_balance': float(income) - float(expense), 'total_samples': total_samples, 'total_staff': total_staff})
    except Department.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Department not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
def reports_api(request):
    try:
        total_patients = Patient.objects.count()
        total_appointments = Appointment.objects.count()
        completed_appointments = Appointment.objects.filter(status='Completed').count()
        total_staff = Staff.objects.count()
        income = Finance.objects.filter(transaction_type='Income').aggregate(total=models.Sum('amount'))['total'] or 0
        expense = Finance.objects.filter(transaction_type='Expense').aggregate(total=models.Sum('amount'))['total'] or 0
        revenue = float(income) - float(expense)
        success_rate = int((completed_appointments / total_appointments) * 100) if total_appointments > 0 else 0
        return JsonResponse({'success': True, 'totalPatients': total_patients, 'totalAppointments': total_appointments, 'completedAppointments': completed_appointments, 'revenue': revenue, 'successRate': success_rate, 'staffCount': total_staff, 'totalIncome': float(income), 'totalExpense': float(expense)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
def departments_api(request):
    try:
        departments = Department.objects.all().values('id', 'name', 'description', 'head')
        return JsonResponse({'success': True, 'departments': list(departments)})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

urlpatterns = [
    path('api/login/', login_api, name='api_login'),
    path('api/logout/', logout_api, name='api_logout'),
    path('api/user/', user_info, name='api_user'),
    path('api/users/', users_api, name='api_users'),
    path('api/users/<int:user_id>/', user_detail_api, name='api_user_detail'),
    path('api/patients/', patients_api, name='api_patients'),
    path('api/patients/<int:patient_id>/', patient_detail_api, name='api_patient_detail'),
    path('api/appointments/', appointments_api, name='api_appointments'),
    path('api/appointments/<int:appointment_id>/', appointment_detail_api, name='api_appointment_detail'),
    path('api/staff/', staff_api, name='api_staff'),
    path('api/staff/<int:staff_id>/', staff_detail_api, name='api_staff_detail'),
    path('api/finance/', finance_api, name='api_finance'),
    path('api/finance/<int:finance_id>/', finance_detail_api, name='api_finance_detail'),
    path('api/samples/', samples_api, name='api_samples'),
    path('api/samples/<int:sample_id>/', sample_detail_api, name='api_sample_detail'),
    path('api/lab-results/', lab_results_api, name='api_lab_results'),
    path('api/lab-results/<int:result_id>/', lab_result_detail_api, name='api_lab_result_detail'),
    path('api/department-stats/', department_stats_api, name='api_department_stats'),
    path('api/reports/', reports_api, name='api_reports'),
    path('api/departments/', departments_api, name='api_departments'),
    
    path('admin/', admin.site.urls),
    
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('users/', TemplateView.as_view(template_name='users.html'), name='users'),
    path('patients/', TemplateView.as_view(template_name='patients.html'), name='patients'),
    path('appointments/', TemplateView.as_view(template_name='appointments.html'), name='appointments'),
    path('staff/', TemplateView.as_view(template_name='staff.html'), name='staff'),
    path('reports/', TemplateView.as_view(template_name='reports.html'), name='reports'),
    path('finance/', TemplateView.as_view(template_name='finance.html'), name='finance'),
    path('settings/', TemplateView.as_view(template_name='settings.html'), name='settings'),
    path('departments/', TemplateView.as_view(template_name='departments.html'), name='departments'),
    path('department-dashboard/', TemplateView.as_view(template_name='department-dashboard.html'), name='department_dashboard'),
    
    # Department pages - WITHOUT .html extension
    path('reception_real/', TemplateView.as_view(template_name='reception_real.html'), name='reception_real'),
    path('opd_real/', TemplateView.as_view(template_name='opd_real.html'), name='opd_real'),
    path('fertility_real/', TemplateView.as_view(template_name='fertility_real.html'), name='fertility_real'),
    path('embryology_real/', TemplateView.as_view(template_name='embryology_real.html'), name='embryology_real'),
    path('andrology_real/', TemplateView.as_view(template_name='andrology_real.html'), name='andrology_real'),
    path('ivf_real/', TemplateView.as_view(template_name='ivf_real.html'), name='ivf_real'),
    path('ultrasound_real/', TemplateView.as_view(template_name='ultrasound_real.html'), name='ultrasound_real'),
    path('nursing_real/', TemplateView.as_view(template_name='nursing_real.html'), name='nursing_real'),
    path('pharmacy_real/', TemplateView.as_view(template_name='pharmacy_real.html'), name='pharmacy_real'),
    path('finance_real/', TemplateView.as_view(template_name='finance_real.html'), name='finance_real'),
    path('lab_real/', TemplateView.as_view(template_name='lab_real.html'), name='lab_real'),
    path('cryobank_real/', TemplateView.as_view(template_name='cryobank_real.html'), name='cryobank_real'),
    path('hr_real/', TemplateView.as_view(template_name='hr_real.html'), name='hr_real'),
    path('admin_real/', TemplateView.as_view(template_name='admin_real.html'), name='admin_real'),
    path('counseling_real/', TemplateView.as_view(template_name='counseling_real.html'), name='counseling_real'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

