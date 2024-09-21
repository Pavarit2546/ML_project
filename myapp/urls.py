from django.urls import path
from . import views

urlpatterns = [
    path('add-patient/', views.add_patient, name='add_patient'),
    path('success/', views.success_view, name='success'),
    path('/patient-list/', views.patient_list, name='patient_list'),# เพจหลังจากบันทึกข้อมูลสำเร็จ
]


