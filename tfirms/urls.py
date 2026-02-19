from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
import dashboard.views
from django.views.generic import TemplateView
from accounts import views as account_views
from django.contrib.admin.views.decorators import staff_member_required
import dashboard.views

# Then in urlpatterns, before admin:

# Admin site customization
admin.site.site_header = "TFICMS - Admin Panel"
admin.site.site_title = "TFICMS Admin"
admin.site.index_title = "Welcome to TFICMS Management System"

schema_view = get_schema_view(
    openapi.Info(
        title="TFICMS API",
        default_version='v1',
        description="Tunajali Fertility & IVF Clinic Management System",
        contact=openapi.Contact(email="info@tficms.local"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
      path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # Root path
        # Root path - Home page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # ==================== AUTHENTICATION ====================
    # Login Portal (department selection)
    path('login/', TemplateView.as_view(template_name='accounts/login_portal.html'), name='login_portal'),
    
    # Department-specific login pages
    path('login/reception/', account_views.reception_login, name='reception_login'),
    path('login/opd/', account_views.opd_login, name='opd_login'),
    path('login/fertility/', account_views.fertility_consultation_login, name='fertility_login'),
    path('login/ivf/', account_views.ivf_login, name='ivf_login'),
    path('login/andrology/', account_views.andrology_lab_login, name='andrology_login'),
    path('login/embryology/', account_views.embryology_lab_login, name='embryology_login'),
    path('login/ultrasound/', account_views.ultrasound_login, name='ultrasound_login'),
    path('login/nursing/', account_views.nursing_login, name='nursing_login'),
    path('login/pharmacy/', account_views.pharmacy_login, name='pharmacy_login'),
    path('login/billing/', account_views.billing_login, name='billing_login'),
    path('login/lab/', account_views.general_lab_login, name='general_lab_login'),
    path('login/counseling/', account_views.counseling_login, name='counseling_login'),
    path('login/cryobank/', account_views.cryobank_login, name='cryobank_login'),
    path('login/hr/', account_views.hr_login, name='hr_login'),
    path('login/admin/', account_views.admin_login, name='admin_login'),
    
    # Department dashboards
    path('dashboard/reception/', account_views.reception_dashboard, name='reception_dashboard'),
    path('dashboard/opd/', account_views.opd_dashboard, name='opd_dashboard'),
    path('dashboard/fertility/', account_views.fertility_consultation_dashboard, name='fertility_dashboard'),
    path('dashboard/ivf/', account_views.ivf_dashboard, name='ivf_dashboard'),
    path('dashboard/andrology/', account_views.andrology_lab_dashboard, name='andrology_dashboard'),
    path('dashboard/embryology/', account_views.embryology_lab_dashboard, name='embryology_dashboard'),
    path('dashboard/ultrasound/', account_views.ultrasound_dashboard, name='ultrasound_dashboard'),
    path('dashboard/nursing/', account_views.nursing_dashboard, name='nursing_dashboard'),
    path('dashboard/pharmacy/', account_views.pharmacy_dashboard, name='pharmacy_dashboard'),
    path('dashboard/billing/', account_views.billing_dashboard, name='billing_dashboard'),
    path('dashboard/lab/', account_views.general_lab_dashboard, name='general_lab_dashboard'),
    path('dashboard/counseling/', account_views.counseling_dashboard, name='counseling_dashboard'),
    path('dashboard/cryobank/', account_views.cryobank_dashboard, name='cryobank_dashboard'),
    path('dashboard/hr/', account_views.hr_dashboard, name='hr_dashboard'),
    path('dashboard/admin/', account_views.admin_dashboard, name='admin_dashboard_dept'),
    
    # Standard auth URLs
    path('accounts/login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login_portal'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # ==================== ADMIN ====================
    path('admin/', admin.site.urls),

    # ==================== API DOCUMENTATION ====================
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

      # ==================== DASHBOARDS ====================
    path('dashboard/', dashboard.views.admin_dashboard, name='admin-dashboard'),

    # ==================== API ENDPOINTS ====================
    path('api/hr/', include('hr_payroll.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/audit/', include('audit.urls')),
    path('api/billing/', include('billing.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/cryobank/', include('cryobank.urls')),
    path('api/andrology-lab/', include('andrology_lab.urls')),
    path('api/embryology-lab/', include('embryology_lab.urls')),
    path('api/ivf/', include('ivf.urls')),
    path('patients/', include('patients.urls_ui')),
    path('api/patients/', include('patients.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)