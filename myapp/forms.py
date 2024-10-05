from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'systolic_bp', 'diastolic_bp', 'blood_sugar', 'body_temp', 'heart_rate']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'ชื่อจริง', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'นามสกุล', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'อายุเป็นปี', 'class': 'form-control'}),
            'systolic_bp': forms.NumberInput(attrs={'placeholder': 'หน่วย: mmHg', 'class': 'form-control'}),
            'diastolic_bp': forms.NumberInput(attrs={'placeholder': 'หน่วย: mmHg', 'class': 'form-control'}),
            'blood_sugar': forms.NumberInput(attrs={'placeholder': 'หน่วย mg/dL', 'class': 'form-control'}),
            'body_temp': forms.NumberInput(attrs={'placeholder': 'หน่วย: °F', 'class': 'form-control'}),
            'heart_rate': forms.NumberInput(attrs={'placeholder': 'หน่วย: ครั้งต่อนาที หรือ bpm - beats per minute', 'class': 'form-control'}),
        }
