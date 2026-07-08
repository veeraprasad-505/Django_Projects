from django.urls import path
from . import views

urlpatterns = [
    path('appointments/add/', views.add_appointment, name='add-appointment'),
    path('appointments/', views.get_appointments, name='get-appointments'),
    path('appointments/update/<int:id>/', views.update_appointment, name='update-appointment'),
    path('appointments/delete/<int:id>/', views.delete_appointment, name='delete-appointment'),
]
