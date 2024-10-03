from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient
import pandas as pd
import pickle

# โหลดโมเดลที่คุณสร้างไว้
with open('best_DT_model.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = form.cleaned_data

            # สร้างข้อมูล dataframe สำหรับทำนายผล
            data = {
                'Age': [patient_data['age']],
                'SystolicBP': [patient_data['systolic_bp']],
                'DiastolicBP': [patient_data['diastolic_bp']],
                'BS': [patient_data['blood_sugar']],
                'BodyTemp': [patient_data['body_temp']],
                'HeartRate': [patient_data['heart_rate']]
            }
            df = pd.DataFrame(data)

            # ใช้โมเดลในการทำนาย
            prediction = model.predict(df)

            # บันทึกข้อมูลและแสดงผลการทำนาย
            form.save()
            
            patient = form.save(commit=False)
            patient.risk_level = str(prediction[0]) # บันทึกผลการทำนายลงในฟิลด์ risk_level
            patient.save()
            context = {
                'result' : prediction
            }
            return render(request, 'success.html', {'patient': patient, 'result': patient.risk_level})
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return redirect('patient_list')