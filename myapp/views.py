from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # เปลี่ยนเส้นทางหลังบันทึกข้อมูลสำเร็จ
    else:
        form = PatientForm()
    
    return render(request, 'add_patient.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')