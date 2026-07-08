from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'specialization', 'experience', 'phone', 'email', 'consultation_fee']
