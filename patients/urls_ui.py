from django.urls import path
from . import views_ui

app_name = "patients"

urlpatterns = [
    path('', views_ui.patient_list, name="patient_list"),
    path('new/', views_ui.patient_create, name="patient_create"),
    path('view/<int:pk>/', views_ui.patient_detail, name="patient_detail"),
]