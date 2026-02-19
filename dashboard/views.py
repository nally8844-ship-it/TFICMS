import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    """
    Dashboard view showing all 15 departments
    """
    
    departments = [
        {
            'name': '🎫 Front Office / Reception',
            'slug': 'reception',
            'description': 'Patient entry & coordination center',
            'color': '#667eea',
            'url': '#',
        },
        {
            'name': '🏥 Outpatient Department (OPD)',
            'slug': 'opd',
            'description': 'Clinical consultation & documentation',
            'color': '#48bb78',
            'url': '#',
        },
        {
            'name': '🔍 Fertility Consultation Unit',
            'slug': 'fertility',
            'description': 'Infertility assessment & monitoring',
            'color': '#ed8936',
            'url': '#',
        },
        {
            'name': '🧬 IVF & ART Department',
            'slug': 'ivf',
            'description': 'IVF cycle execution & management',
            'color': '#9f7aea',
            'url': '#',
        },
        {
            'name': '🔬 Andrology Laboratory',
            'slug': 'andrology',
            'description': 'Male fertility diagnostics & sperm handling',
            'color': '#3182ce',
            'url': '#',
        },
        {
            'name': '🥚 Embryology Laboratory',
            'slug': 'embryology',
            'description': 'Embryo development & cryostorage',
            'color': '#e53e3e',
            'url': '#',
        },
        {
            'name': '📡 Ultrasound & Imaging Department',
            'slug': 'ultrasound',
            'description': 'Diagnostic imaging & monitoring',
            'color': '#38b2ac',
            'url': '#',
        },
        {
            'name': '👩‍⚕️ Nursing Department',
            'slug': 'nursing',
            'description': 'Clinical support & patient care',
            'color': '#f6ad55',
            'url': '#',
        },
        {
            'name': '💊 Pharmacy Department',
            'slug': 'pharmacy',
            'description': 'Drug & inventory management',
            'color': '#ecc94b',
            'url': '#',
        },
        {
            'name': '💰 Finance & Billing Department',
            'slug': 'billing',
            'description': 'Revenue & financial management',
            'color': '#48bb78',
            'url': '#',
        },
        {
            'name': '🧪 General Laboratory (Diagnostics)',
            'slug': 'lab',
            'description': 'Supporting medical testing',
            'color': '#4299e1',
            'url': '#',
        },
        {
            'name': '💭 Counseling & Psychology Unit',
            'slug': 'counseling',
            'description': 'Emotional & psychological support',
            'color': '#b19cd9',
            'url': '#',
        },
        {
            'name': '❄️ Cryobank Management',
            'slug': 'cryobank',
            'description': 'Gamete & embryo storage control',
            'color': '#4fd1c5',
            'url': '#',
        },
        {
            'name': '👔 Human Resource (HR)',
            'slug': 'hr',
            'description': 'Staff & workforce management',
            'color': '#fc8181',
            'url': '#',
        },
        {
            'name': '⚙️ Administration & Management',
            'slug': 'admin',
            'description': 'Oversight & performance monitoring',
            'color': '#667eea',
            'url': '#',
        },
    ]
    
    context = {
        'departments': departments,
    }
    
    return render(request, 'dashboard/departments.html', context)