from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# ==================== LOGIN VIEWS ====================

@require_http_methods(["GET", "POST"])
def reception_login(request):
    """Login for Reception / Front Office"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user belongs to this department OR is superuser
            if user.department == 'reception' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Reception.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Reception', 'error': error})


@require_http_methods(["GET", "POST"])
def opd_login(request):
    """Login for OPD (Outpatient Department)"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'opd' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to OPD.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'OPD', 'error': error})


@require_http_methods(["GET", "POST"])
def fertility_consultation_login(request):
    """Login for Fertility Consultation Unit"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'fertility_consultation' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Fertility Consultation.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Fertility Consultation', 'error': error})


@require_http_methods(["GET", "POST"])
def ivf_login(request):
    """Login for IVF & ART Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'ivf' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to IVF.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'IVF & ART', 'error': error})


@require_http_methods(["GET", "POST"])
def andrology_lab_login(request):
    """Login for Andrology Laboratory"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'andrology_lab' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Andrology Lab.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Andrology Laboratory', 'error': error})


@require_http_methods(["GET", "POST"])
def embryology_lab_login(request):
    """Login for Embryology Laboratory"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'embryology_lab' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Embryology Lab.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Embryology Laboratory', 'error': error})


@require_http_methods(["GET", "POST"])
def ultrasound_login(request):
    """Login for Ultrasound & Imaging Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'ultrasound' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Ultrasound.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Ultrasound & Imaging', 'error': error})


@require_http_methods(["GET", "POST"])
def nursing_login(request):
    """Login for Nursing Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'nursing' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Nursing.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Nursing', 'error': error})


@require_http_methods(["GET", "POST"])
def pharmacy_login(request):
    """Login for Pharmacy Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'pharmacy' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Pharmacy.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Pharmacy', 'error': error})


@require_http_methods(["GET", "POST"])
def billing_login(request):
    """Login for Finance & Billing Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'billing' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Billing.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Billing', 'error': error})


@require_http_methods(["GET", "POST"])
def general_lab_login(request):
    """Login for General Laboratory"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'general_lab' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to General Lab.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'General Laboratory', 'error': error})


@require_http_methods(["GET", "POST"])
def counseling_login(request):
    """Login for Counseling & Psychology Unit"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'counseling' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Counseling.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Counseling & Psychology', 'error': error})


@require_http_methods(["GET", "POST"])
def cryobank_login(request):
    """Login for Cryobank Management"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'cryobank' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to Cryobank.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Cryobank', 'error': error})


@require_http_methods(["GET", "POST"])
def hr_login(request):
    """Login for HR Department"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.department == 'hr' or user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. You cannot login to HR.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'HR', 'error': error})


@require_http_methods(["GET", "POST"])
def admin_login(request):
    """Login for Administration & Management"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser or user.department == 'admin':
                login(request, user)
                return redirect('admin-dashboard')
            else:
                error = f'❌ Access Denied! Your account is assigned to {user.get_department_display()}. Only admins can login here.'
        else:
            error = '❌ Invalid username or password.'
    
    return render(request, 'accounts/login.html', {'department': 'Administration', 'error': error})


# ==================== DASHBOARD VIEWS ====================

@login_required
def reception_dashboard(request):
    return render(request, 'dashboard/reception_dashboard.html')

@login_required
def opd_dashboard(request):
    return render(request, 'dashboard/opd_dashboard.html')

@login_required
def fertility_consultation_dashboard(request):
    return render(request, 'dashboard/fertility_dashboard.html')

@login_required
def ivf_dashboard(request):
    return render(request, 'dashboard/ivf_dashboard.html')

@login_required
def andrology_lab_dashboard(request):
    return render(request, 'dashboard/andrology_dashboard.html')

@login_required
def embryology_lab_dashboard(request):
    return render(request, 'dashboard/embryology_dashboard.html')

@login_required
def ultrasound_dashboard(request):
    return render(request, 'dashboard/ultrasound_dashboard.html')

@login_required
def nursing_dashboard(request):
    return render(request, 'dashboard/nursing_dashboard.html')

@login_required
def pharmacy_dashboard(request):
    return render(request, 'dashboard/pharmacy_dashboard.html')

@login_required
def billing_dashboard(request):
    return render(request, 'dashboard/billing_dashboard.html')

@login_required
def general_lab_dashboard(request):
    return render(request, 'dashboard/general_lab_dashboard.html')

@login_required
def counseling_dashboard(request):
    return render(request, 'dashboard/counseling_dashboard.html')

@login_required
def cryobank_dashboard(request):
    return render(request, 'dashboard/cryobank_dashboard.html')

@login_required
def hr_dashboard(request):
    return render(request, 'dashboard/hr_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')