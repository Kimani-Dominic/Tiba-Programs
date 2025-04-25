from django.db import models

from django.contrib.auth import get_user_model

from programs.models import HealthProgram


STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
)

User = get_user_model()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_appointments")
    # program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE)
    program = models.ForeignKey(HealthProgram, on_delete=models.SET_NULL, null=True, blank=True)  # program field
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.doctor.username} at {self.appointment_time} for {self.user.username}"
