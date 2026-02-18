from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment, next_queue_number
from datetime import date

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all().select_related('patient','doctor')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.queue_number = next_queue_number(obj.scheduled_time.date())
            obj.created_by = request.user
            obj.save()
            # TODO: trigger SMS/Email reminders via notifications/Celery
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})