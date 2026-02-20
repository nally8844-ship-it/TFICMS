from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            from django.contrib.auth import authenticate, login
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return JsonResponse({'success': True})
            return JsonResponse({'success': False, 'message': 'Invalid'}, status=401)
        except:
            return JsonResponse({'success': False}, status=500)
    return JsonResponse({'success': False}, status=405)

urlpatterns = [
    path('api/login/', login_api),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),
    path('departments/', TemplateView.as_view(template_name='departments.html')),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)