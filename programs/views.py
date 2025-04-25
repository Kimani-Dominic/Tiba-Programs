from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied


from programs.models import *
from programs.serializers import *

class HealthProgramCreateView(generics.CreateAPIView):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if not user.groups.filter(name='doctor').exists():
            raise PermissionDenied("Only doctors can create health programs.")

        serializer.save()
    
class HealthProgramListView(generics.ListAPIView):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_doctor:
            return HealthProgram.objects.all()
        return HealthProgram.objects.none()
    
class ProgramEnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = ProgramEnrollment.objects.all()
    serializer_class = ProgramEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        
        if not user.groups.filter(name='doctor').exists():
             raise PermissionDenied("Only users with doctor role can enroll patients into health programs.")

        serializer.save()
        

class PatientHealthRecordListView(generics.ListAPIView):
    serializer_class = ProgramEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ProgramEnrollment.objects.filter(patient=user)
