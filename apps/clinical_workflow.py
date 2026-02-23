# Clinical Management System Workflow Implementation

class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = []

    def add_medical_history(self, record):
        self.medical_history.append(record)

class Appointment:
    def __init__(self, appointment_id, patient, date, time, doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.time = time
        self.doctor = doctor

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class ClinicalWorkflow:
    def __init__(self):
        self.patients = []
        self.appointments = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_patient_appointments(self, patient_id):
        return [ap for ap in self.appointments if ap.patient.patient_id == patient_id]

# Example usage
if __name__ == '__main__':
    workflow = ClinicalWorkflow()
    doctor1 = Doctor(1, 'Dr. Smith', 'Cardiology')
    workflow.add_doctor(doctor1)

    patient1 = Patient(1, 'John Doe', 30, 'Male')
    workflow.add_patient(patient1)

    appointment1 = Appointment(1, patient1, '2026-02-25', '10:00 AM', doctor1)
    workflow.schedule_appointment(appointment1)

    print(f"Appointments for {patient1.name}: {workflow.get_patient_appointments(patient1.patient_id)}")
