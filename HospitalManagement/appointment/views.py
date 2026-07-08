from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Appointment
from .serializers import AppointmentSerializer


@api_view(['POST'])
def add_appointment(request):
    """Add a new appointment record."""
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Appointment Added Successfully",
                "appointment": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_appointments(request):
    """Retrieve all appointment records."""
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_appointment(request, id):
    """Update an existing appointment's details by ID."""
    appointment = get_object_or_404(Appointment, id=id)
    serializer = AppointmentSerializer(appointment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Appointment Updated Successfully",
                "appointment": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_appointment(request, id):
    """Delete an appointment record by ID."""
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return Response(
        {"message": "Appointment Deleted Successfully"},
        status=status.HTTP_200_OK
    )
