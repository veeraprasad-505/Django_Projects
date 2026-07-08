from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor
from .serializers import DoctorSerializer


@api_view(['POST'])
def add_doctor(request):
    """Add a new doctor record."""
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Doctor Added Successfully",
                "doctor": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_doctors(request):
    """Retrieve all doctor records."""
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_doctor(request, id):
    """Update an existing doctor's details by ID."""
    doctor = get_object_or_404(Doctor, id=id)
    serializer = DoctorSerializer(doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Doctor Updated Successfully",
                "doctor": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_doctor(request, id):
    """Delete a doctor record by ID."""
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return Response(
        {"message": "Doctor Deleted Successfully"},
        status=status.HTTP_200_OK
    )
