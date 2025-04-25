from django.db import models

from Auth.models import User
from appointments.models import Appointment
from programs.models import HealthProgram

user = User

class MedicalRecord(models.Model):
    patient = models.ForeignKey(user, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='medical_record')
    # program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE, related_name="medical_records")
    program = models.ForeignKey(HealthProgram, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Medical Record for {self.patient.username} - {self.appointment.appointment_time} - for program: {self.program.name}"
