from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='trainers_index'),
]
