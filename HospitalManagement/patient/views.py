from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer


@api_view(['POST'])
def add_patient(request):
    """Add a new patient record."""
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Patient Added Successfully",
                "patient": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_patients(request):
    """Retrieve all patient records."""
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_patient(request, id):
    """Update an existing patient's details by ID."""
    patient = get_object_or_404(Patient, id=id)
    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Patient Updated Successfully",
                "patient": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_patient(request, id):
    """Delete a patient record by ID."""
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return Response(
        {"message": "Patient Deleted Successfully"},
        status=status.HTTP_200_OK
    )
