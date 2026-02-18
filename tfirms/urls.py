from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
import dashboard.views

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
    # Root path - redirect to dashboard or admin
    path('', dashboard.views.admin_dashboard, name='home'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/hr/', include('hr_payroll.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/audit/', include('audit.urls')),
    path('dashboard/', dashboard.views.admin_dashboard, name='admin-dashboard'),
    path('api/billing/', include('billing.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/cryobank/', include('cryobank.urls')),
    path('api/andrology-lab/', include('andrology_lab.urls')),
    path('api/embryology-lab/', include('embryology_lab.urls')),
    path('api/ivf/', include('ivf.urls')),
    path('patients/', include('patients.urls_ui')),
    path('api/patients/', include('patients.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)