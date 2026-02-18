from django.shortcuts import render
from django.http import HttpResponse
from patients.models import Patient
from appointments.models import Appointment
from billing.models import Invoice
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from io import BytesIO
import datetime

def patient_report_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    patients = Patient.objects.all()[:100]
    y = 800
    p.drawString(100, y, "Patient Report")
    y -= 40
    for pt in patients:
        p.drawString(100, y, f"{pt.unique_id} - {pt.first_name} {pt.last_name} DOB:{pt.date_of_birth}")
        y -= 20
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def patient_report_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Patients"
    ws.append(['Unique ID','Name','DOB','Phone'])
    for pt in Patient.objects.all():
        ws.append([pt.unique_id, f"{pt.first_name} {pt.last_name}", str(pt.date_of_birth), pt.phone])
    out = BytesIO()
    wb.save(out)
    out.seek(0)
    response = HttpResponse(out, content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="patients_{datetime.date.today()}.xlsx"'
    return response

def kpi_dashboard(request):
    return render(request, "reports/report_dashboard.html", {
        # add analytics and Chart.js data
    })