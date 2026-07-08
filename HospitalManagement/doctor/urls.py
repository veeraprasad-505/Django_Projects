from django.urls import path
from . import views

urlpatterns = [
    path('doctors/add/', views.add_doctor, name='add-doctor'),
    path('doctors/', views.get_doctors, name='get-doctors'),
    path('doctors/update/<int:id>/', views.update_doctor, name='update-doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete-doctor'),
]
