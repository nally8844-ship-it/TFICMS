from django.urls import path
from . import views

urlpatterns = [
    path('patients/pdf/', views.patient_report_pdf, name='patients_pdf'),
    path('patients/excel/', views.patient_report_excel, name='patients_excel'),
    path('dashboard/', views.kpi_dashboard, name='kpi_dashboard'),
]