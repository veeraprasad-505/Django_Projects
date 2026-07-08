from django.db import models


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    disease = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.patient_name
