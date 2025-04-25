from django.db import models

from Auth.models import User

AVAILABLE_HEALTH_PROGRAMS = (
    ("HIV", "HIV Program"),
    ("TB", "Tuberculosis Program"),
    ("MALARIA", "Malaria Program"),
    ("ANTENATAL", "Antenatal Care"),
    ("IMMUNIZATION", "Immunization Program"),
    ("NUTRITION", "Nutrition Program"),
    ("MENTAL_HEALTH", "Mental Health Program"),
    ("DIABETES", "Diabetes Management"),
    ("HYPERTENSION", "Hypertension Program"),
    ("GENERAL_OPD", "General Outpatient Services"),
)


class HealthProgram(models.Model):
    name = models.CharField(choices=AVAILABLE_HEALTH_PROGRAMS, max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return dict(AVAILABLE_HEALTH_PROGRAMS).get(self.name)
    
class ProgramEnrollment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='programs')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} -> {self.program}"
    