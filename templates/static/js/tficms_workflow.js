// TFICMS WORKFLOW - SIMPLE & WORKING
class TFICMSWorkflow {
    constructor() {
        this.loadData();
    }

    loadData() {
        this.patients = JSON.parse(localStorage.getItem('tficms_patients')) || [];
        this.appointments = JSON.parse(localStorage.getItem('tficms_appointments')) || [];
        this.assignments = JSON.parse(localStorage.getItem('tficms_assignments')) || [];
    }

    registerPatient(firstName, lastName, email, phone, age, gender) {
        const patient = {
            id: 'P' + Date.now(),
            firstName: firstName,
            lastName: lastName,
            email: email,
            phone: phone,
            age: age,
            gender: gender,
            registrationDate: new Date().toLocaleString(),
            status: 'Active'
        };

        this.patients.push(patient);
        localStorage.setItem('tficms_patients', JSON.stringify(this.patients));
        console.log('Patient registered:', patient);
        return patient;
    }

    assignPatientToDept(patientId, department, staff, notes) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) {
            console.log('Patient not found:', patientId);
            return null;
        }

        const assignment = {
            id: 'ASN-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            patientEmail: patient.email,
            patientPhone: patient.phone,
            department: department,
            staff: staff,
            notes: notes,
            assignedDate: new Date().toLocaleString(),
            status: 'Pending'
        };

        this.assignments.push(assignment);
        localStorage.setItem('tficms_assignments', JSON.stringify(this.assignments));
        console.log('Patient assigned:', assignment);
        return assignment;
    }

    getPatientsForDepartment(department) {
        this.loadData();
        return this.assignments.filter(a => a.department === department);
    }

    getAllPatients() {
        this.loadData();
        return this.patients;
    }

    refresh() {
        this.loadData();
    }
}

// Create and expose globally
const workflow = new TFICMSWorkflow();
console.log('Workflow initialized');
