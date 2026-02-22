// TFICMS COMPLETE WORKFLOW ENGINE
// ================================
// Handles all 15 departments with complete workflow automation

class TFICMSWorkflow {
    constructor() {
        this.patients = JSON.parse(localStorage.getItem('tficms_patients')) || [];
        this.appointments = JSON.parse(localStorage.getItem('tficms_appointments')) || [];
        this.consultations = JSON.parse(localStorage.getItem('tficms_consultations')) || [];
        this.prescriptions = JSON.parse(localStorage.getItem('tficms_prescriptions')) || [];
        this.labOrders = JSON.parse(localStorage.getItem('tficms_lab_orders')) || [];
        this.labResults = JSON.parse(localStorage.getItem('tficms_lab_results')) || [];
        this.ivfCycles = JSON.parse(localStorage.getItem('tficms_ivf_cycles')) || [];
        this.embryos = JSON.parse(localStorage.getItem('tficms_embryos')) || [];
        this.medications = JSON.parse(localStorage.getItem('tficms_medications')) || [];
        this.invoices = JSON.parse(localStorage.getItem('tficms_invoices')) || [];
        this.emr = JSON.parse(localStorage.getItem('tficms_emr')) || [];
    }

    // ========== PHASE 1: RECEPTION - PATIENT REGISTRATION ==========
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

        // Initialize EMR
        const emrRecord = {
            patientId: patient.id,
            patientName: firstName + ' ' + lastName,
            createdDate: new Date().toLocaleString(),
            consultations: [],
            labTests: [],
            diagnoses: [],
            prescriptions: [],
            ivfCycles: []
        };
        this.emr.push(emrRecord);
        localStorage.setItem('tficms_emr', JSON.stringify(this.emr));

        return patient;
    }

    scheduleAppointment(patientId, department, doctorName, appointmentDate, notes) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const appointment = {
            id: 'APT-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            department: department,
            doctor: doctorName,
            appointmentDate: appointmentDate,
            notes: notes,
            createdDate: new Date().toLocaleString(),
            status: 'Scheduled',
            queueNumber: Math.floor(Math.random() * 100) + 1
        };

        this.appointments.push(appointment);
        localStorage.setItem('tficms_appointments', JSON.stringify(this.appointments));

        return appointment;
    }

    // ========== PHASE 2: OPD - DOCTOR CONSULTATION ==========
    recordConsultation(patientId, doctorName, symptoms, diagnosis, notes) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const consultation = {
            id: 'CON-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            doctor: doctorName,
            symptoms: symptoms,
            diagnosis: diagnosis,
            notes: notes,
            consultationDate: new Date().toLocaleString(),
            status: 'Completed'
        };

        this.consultations.push(consultation);
        localStorage.setItem('tficms_consultations', JSON.stringify(this.consultations));

        // Update EMR
        this.updateEMR(patientId, 'consultation', consultation);

        return consultation;
    }

    // ========== ORDER LAB TEST (From OPD) ==========
    orderLabTest(patientId, testType, indication, priority, doctorName) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const labOrder = {
            id: 'LAB-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            testType: testType, // Hormonal, Semen Analysis, Blood Test, etc.
            indication: indication,
            orderedBy: doctorName,
            orderedDate: new Date().toLocaleString(),
            priority: priority,
            status: 'Pending Sample Collection'
        };

        this.labOrders.push(labOrder);
        localStorage.setItem('tficms_lab_orders', JSON.stringify(this.labOrders));

        // Update EMR
        this.updateEMR(patientId, 'lab_order', labOrder);

        return labOrder;
    }

    // ========== PRESCRIBE MEDICATION (From OPD) ==========
    prescribeMedication(patientId, medicineName, dosage, quantity, instructions, doctorName) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const prescription = {
            id: 'RX-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            medicineName: medicineName,
            dosage: dosage,
            quantity: quantity,
            instructions: instructions,
            prescribedBy: doctorName,
            prescribedDate: new Date().toLocaleString(),
            status: 'Pending Dispense'
        };

        this.prescriptions.push(prescription);
        localStorage.setItem('tficms_prescriptions', JSON.stringify(this.prescriptions));

        // Update EMR
        this.updateEMR(patientId, 'prescription', prescription);

        return prescription;
    }

    // ========== PHASE 3: FERTILITY CONSULTATION ==========
    createFertilityCoupleProfile(wifeId, husbandName, husbandAge, infertilityType, duration) {
        const wife = this.patients.find(p => p.id === wifeId);
        if (!wife) return null;

        const coupleProfile = {
            id: 'COUPLE-' + Date.now(),
            wifeId: wifeId,
            wifeName: wife.firstName + ' ' + wife.lastName,
            husbandName: husbandName,
            husbandAge: husbandAge,
            infertilityType: infertilityType, // Primary, Secondary, Male Factor, etc.
            durationYears: duration,
            createdDate: new Date().toLocaleString(),
            status: 'Active'
        };

        localStorage.setItem('tficms_couple_profile', JSON.stringify(coupleProfile));
        this.updateEMR(wifeId, 'fertility_profile', coupleProfile);

        return coupleProfile;
    }

    recordFertilityAssessment(patientId, ovulationStatus, uterineStatus, semenResult, spermCount, assessment) {
        const assessment_record = {
            id: 'FERT-' + Date.now(),
            patientId: patientId,
            ovulationStatus: ovulationStatus,
            uterineStatus: uterineStatus,
            semenResult: semenResult,
            spermCount: spermCount,
            assessment: assessment,
            assessmentDate: new Date().toLocaleString()
        };

        this.updateEMR(patientId, 'fertility_assessment', assessment_record);
        return assessment_record;
    }

    // ========== PHASE 4: LAB RESULTS ==========
    recordLabResult(labOrderId, results, technician) {
        const labOrder = this.labOrders.find(l => l.id === labOrderId);
        if (!labOrder) return null;

        labOrder.status = 'Completed';
        labOrder.results = results;
        labOrder.completedDate = new Date().toLocaleString();
        labOrder.completedBy = technician;

        localStorage.setItem('tficms_lab_orders', JSON.stringify(this.labOrders));

        // Store results
        const result_record = {
            id: 'RESULT-' + Date.now(),
            labOrderId: labOrderId,
            patientId: labOrder.patientId,
            testType: labOrder.testType,
            results: results,
            recordedDate: new Date().toLocaleString()
        };

        this.labResults.push(result_record);
        localStorage.setItem('tficms_lab_results', JSON.stringify(this.labResults));

        // Update EMR
        this.updateEMR(labOrder.patientId, 'lab_result', result_record);

        return result_record;
    }

    // ========== PHASE 5: IVF CYCLE INITIATION ==========
    initiateIVFCycle(patientId, protocol, startDate, fertility_specialist) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const ivfCycle = {
            id: 'IVF-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            protocol: protocol, // Long, Short, Mild, Natural
            startDate: startDate,
            fertilitySpecialist: fertility_specialist,
            status: 'Stimulation',
            createdDate: new Date().toLocaleString(),
            milestones: {
                eggRetrieval: null,
                fertilization: null,
                embryoTransfer: null,
                pregnancyTest: null
            }
        };

        this.ivfCycles.push(ivfCycle);
        localStorage.setItem('tficms_ivf_cycles', JSON.stringify(this.ivfCycles));

        // Update EMR
        this.updateEMR(patientId, 'ivf_cycle', ivfCycle);

        return ivfCycle;
    }

    // ========== PHASE 6: EMBRYOLOGY - EGG RETRIEVAL & FERTILIZATION ==========
    recordEggRetrieval(ivfCycleId, oocytesCollected, embryologist) {
        const ivfCycle = this.ivfCycles.find(c => c.id === ivfCycleId);
        if (!ivfCycle) return null;

        ivfCycle.status = 'Fertilization';
        ivfCycle.milestones.eggRetrieval = {
            date: new Date().toLocaleString(),
            oocytesCollected: oocytesCollected,
            embryologist: embryologist
        };

        localStorage.setItem('tficms_ivf_cycles', JSON.stringify(this.ivfCycles));
        this.updateEMR(ivfCycle.patientId, 'egg_retrieval', ivfCycle.milestones.eggRetrieval);

        return ivfCycle;
    }

    recordFertilization(ivfCycleId, method, fertilizedOocytes, embryologist) {
        const ivfCycle = this.ivfCycles.find(c => c.id === ivfCycleId);
        if (!ivfCycle) return null;

        ivfCycle.milestones.fertilization = {
            date: new Date().toLocaleString(),
            method: method, // IVF, ICSI
            fertilizedOocytes: fertilizedOocytes,
            embryologist: embryologist
        };

        localStorage.setItem('tficms_ivf_cycles', JSON.stringify(this.ivfCycles));
        this.updateEMR(ivfCycle.patientId, 'fertilization', ivfCycle.milestones.fertilization);

        return ivfCycle;
    }

    recordEmbryoDevelopment(ivfCycleId, dayNumber, grading, embryoCount) {
        const ivfCycle = this.ivfCycles.find(c => c.id === ivfCycleId);
        if (!ivfCycle) return null;

        const embryoRecord = {
            id: 'EMBRYO-' + Date.now(),
            ivfCycleId: ivfCycleId,
            patientId: ivfCycle.patientId,
            day: dayNumber,
            grading: grading,
            embryoCount: embryoCount,
            recordedDate: new Date().toLocaleString(),
            status: 'Developing'
        };

        this.embryos.push(embryoRecord);
        localStorage.setItem('tficms_embryos', JSON.stringify(this.embryos));

        this.updateEMR(ivfCycle.patientId, 'embryo_development', embryoRecord);

        return embryoRecord;
    }

    // ========== PHASE 7A: EMBRYO TRANSFER ==========
    performEmbryoTransfer(ivfCycleId, embryoDay, gradeTransferred, embryologist) {
        const ivfCycle = this.ivfCycles.find(c => c.id === ivfCycleId);
        if (!ivfCycle) return null;

        ivfCycle.status = 'Post-Transfer';
        ivfCycle.milestones.embryoTransfer = {
            date: new Date().toLocaleString(),
            embryoDay: embryoDay,
            gradeTransferred: gradeTransferred,
            embryologist: embryologist
        };

        localStorage.setItem('tficms_ivf_cycles', JSON.stringify(this.ivfCycles));
        this.updateEMR(ivfCycle.patientId, 'embryo_transfer', ivfCycle.milestones.embryoTransfer);

        return ivfCycle;
    }

    // ========== PHASE 7B: CRYOPRESERVATION ==========
    freezeEmbryo(embryoId, cryoProtocol, tankLocation, consentObtained) {
        const embryo = this.embryos.find(e => e.id === embryoId);
        if (!embryo) return null;

        embryo.status = 'Frozen';
        embryo.freezeDetails = {
            date: new Date().toLocaleString(),
            protocol: cryoProtocol,
            tankLocation: tankLocation,
            consentObtained: consentObtained
        };

        localStorage.setItem('tficms_embryos', JSON.stringify(this.embryos));
        this.updateEMR(embryo.patientId, 'embryo_frozen', embryo.freezeDetails);

        return embryo;
    }

    // ========== PHASE 8: PHARMACY - DISPENSE MEDICATION ==========
    dispenseMedication(prescriptionId, batchNo, expiryDate, pharmacist) {
        const prescription = this.prescriptions.find(p => p.id === prescriptionId);
        if (!prescription) return null;

        prescription.status = 'Dispensed';
        prescription.dispensedDate = new Date().toLocaleString();
        prescription.batchNo = batchNo;
        prescription.expiryDate = expiryDate;
        prescription.dispensedBy = pharmacist;

        localStorage.setItem('tficms_prescriptions', JSON.stringify(this.prescriptions));
        this.updateEMR(prescription.patientId, 'medicine_dispensed', prescription);

        return prescription;
    }

    // ========== PHASE 9: FINANCE - GENERATE INVOICE ==========
    generateInvoice(patientId, serviceType, amount, description) {
        const patient = this.patients.find(p => p.id === patientId);
        if (!patient) return null;

        const invoice = {
            id: 'INV-' + Date.now(),
            patientId: patientId,
            patientName: patient.firstName + ' ' + patient.lastName,
            serviceType: serviceType, // Consultation, IVF, Lab, etc.
            amount: amount,
            description: description,
            invoiceDate: new Date().toLocaleString(),
            status: 'Pending Payment',
            paymentMethod: null,
            paymentDate: null
        };

        this.invoices.push(invoice);
        localStorage.setItem('tficms_invoices', JSON.stringify(this.invoices));

        return invoice;
    }

    recordPayment(invoiceId, paymentMethod, amount) {
        const invoice = this.invoices.find(i => i.id === invoiceId);
        if (!invoice) return null;

        invoice.status = 'Paid';
        invoice.paymentMethod = paymentMethod;
        invoice.paymentDate = new Date().toLocaleString();
        invoice.paidAmount = amount;

        localStorage.setItem('tficms_invoices', JSON.stringify(this.invoices));

        return invoice;
    }

    // ========== EMR MANAGEMENT ==========
    updateEMR(patientId, recordType, data) {
        let emrRecord = this.emr.find(e => e.patientId === patientId);

        if (!emrRecord) {
            const patient = this.patients.find(p => p.id === patientId);
            emrRecord = {
                patientId: patientId,
                patientName: patient ? patient.firstName + ' ' + patient.lastName : 'Unknown',
                createdDate: new Date().toLocaleString(),
                consultations: [],
                labTests: [],
                diagnoses: [],
                prescriptions: [],
                ivfCycles: []
            };
            this.emr.push(emrRecord);
        }

        // Add record to appropriate array
        if (recordType === 'consultation') emrRecord.consultations.push(data);
        else if (recordType === 'lab_order' || recordType === 'lab_result') emrRecord.labTests.push(data);
        else if (recordType === 'prescription' || recordType === 'medicine_dispensed') emrRecord.prescriptions.push(data);
        else if (recordType === 'ivf_cycle') emrRecord.ivfCycles.push(data);

        localStorage.setItem('tficms_emr', JSON.stringify(this.emr));
        return emrRecord;
    }

    getPatientEMR(patientId) {
        return this.emr.find(e => e.patientId === patientId);
    }

    // ========== DASHBOARD QUERIES ==========
    getTasksForDepartment(department) {
        const tasks = {};

        switch(department) {
            case 'RECEPTION':
                tasks.appointments = this.appointments.filter(a => a.status === 'Scheduled');
                break;

            case 'OPD':
                tasks.consultations = this.consultations.filter(c => c.status !== 'Completed');
                tasks.pendingTests = this.labOrders.filter(l => l.status === 'Pending Sample Collection');
                break;

            case 'FERTILITY':
                tasks.coupleProfiles = this.emr.filter(e => e.ivfCycles && e.ivfCycles.length > 0);
                break;

            case 'LAB':
                tasks.pendingTests = this.labOrders.filter(l => l.status === 'Pending Sample Collection' || l.status === 'Sample Collected');
                break;

            case 'EMBRYOLOGY':
                tasks.ivfCycles = this.ivfCycles.filter(c => c.status === 'Fertilization' || c.status === 'Development');
                tasks.embryos = this.embryos.filter(e => e.status === 'Developing');
                break;

            case 'PHARMACY':
                tasks.pendingPrescriptions = this.prescriptions.filter(p => p.status === 'Pending Dispense');
                break;

            case 'FINANCE':
                tasks.pendingInvoices = this.invoices.filter(i => i.status === 'Pending Payment');
                break;
        }

        return tasks;
    }

    // ========== STATISTICS ==========
    getStatistics(department) {
        const stats = {};

        switch(department) {
            case 'RECEPTION':
                stats.totalPatients = this.patients.length;
                stats.todayAppointments = this.appointments.filter(a => a.appointmentDate.includes(new Date().toDateString())).length;
                break;

            case 'OPD':
                stats.totalConsultations = this.consultations.length;
                stats.pendingConsultations = this.consultations.filter(c => c.status !== 'Completed').length;
                break;

            case 'PHARMACY':
                stats.pendingPrescriptions = this.prescriptions.filter(p => p.status === 'Pending Dispense').length;
                stats.dispensedToday = this.prescriptions.filter(p => p.status === 'Dispensed').length;
                break;

            case 'FINANCE':
                stats.totalRevenue = this.invoices.reduce((sum, inv) => sum + (inv.status === 'Paid' ? inv.amount : 0), 0);
                stats.pendingPayments = this.invoices.filter(i => i.status === 'Pending Payment').length;
                break;

            case 'IVF':
                stats.activeCycles = this.ivfCycles.filter(c => c.status !== 'Completed').length;
                stats.pregnancyRate = ((this.ivfCycles.filter(c => c.status === 'Positive').length / this.ivfCycles.length) * 100).toFixed(2) + '%';
                break;
        }

        return stats;
    }
}

// Initialize globally
const workflow = new TFICMSWorkflow();
