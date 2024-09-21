from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'systolic_bp', 'diastolic_bp', 'blood_sugar', 'body_temp', 'heart_rate']
