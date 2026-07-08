from django.urls import path
from . import views

urlpatterns = [
    path('patients/add/', views.add_patient, name='add-patient'),
    path('patients/', views.get_patients, name='get-patients'),
    path('patients/update/<int:id>/', views.update_patient, name='update-patient'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete-patient'),
]
