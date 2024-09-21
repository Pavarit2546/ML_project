from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'systolic_bp', 'diastolic_bp', 'blood_sugar', 'body_temp', 'heart_rate']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'systolic_bp': forms.NumberInput(attrs={'placeholder': 'Systolic BP'}),
            'diastolic_bp': forms.NumberInput(attrs={'placeholder': 'Diastolic BP'}),
            'blood_sugar': forms.NumberInput(attrs={'placeholder': 'Blood Sugar Level'}),
            'body_temp': forms.NumberInput(attrs={'placeholder': 'Body Temperature'}),
            'heart_rate': forms.NumberInput(attrs={'placeholder': 'Heart Rate'}),
        }
