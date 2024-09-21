from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    systolic_bp = models.FloatField()  # Systolic Blood Pressure
    diastolic_bp = models.FloatField()  # Diastolic Blood Pressure
    blood_sugar = models.FloatField()  # Blood glucose levels (BS)
    body_temp = models.FloatField()  # Body Temperature
    heart_rate = models.FloatField()  # Heart Rate

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Age: {self.age}"

