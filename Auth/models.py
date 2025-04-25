from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser): 
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    def assign_role(self, role):
        if role == "doctor":
            self.is_doctor = True
            self.is_patient = False
            doctor_group, _ = Group.objects.get_or_create(name='doctor')
            patient_group, _ = Group.objects.get_or_create(name='patient')
            self.groups.set([doctor_group, patient_group])
        elif role == "patient":
            self.is_doctor = False
            self.is_patient = True
            patient_group, _ = Group.objects.get_or_create(name='patient')
            self.groups.set([patient_group])
        self.save()
