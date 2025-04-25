from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError


from MedicalRecords.models import MedicalRecord
from MedicalRecords.serializers import MedicalRecordSerializer
from appointments.models import Appointment

class MedicalRecordCreateView(generics.CreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if not user.groups.filter(name='doctor').exists():
            raise PermissionError("Only doctors can create medical records.")

        appointment_id = self.request.data.get('appointment')
        if not appointment_id:
            raise ValidationError("Appointment Id is required.")
        
        appointment = get_object_or_404(Appointment, id=appointment_id)
        if MedicalRecord.objects.filter(appointment=appointment).exists():
            raise ValidationError("A medical record for this appointment already exists.")

        serializer.save(
            appointment=appointment,
            patient=appointment.user 
        )
        
  
class PatientMedicalRecordListView(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='patient').exists():
            return MedicalRecord.objects.filter(patient=user)
        elif user.groups.filter(name='doctor').exists():
            return MedicalRecord.objects.all()
        return MedicalRecord.objects.none()

