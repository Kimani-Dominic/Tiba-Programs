from rest_framework import serializers

from appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_time', 'status', 'program','created_at']
        
        def validate_user(self, value):
            if not value:
                raise serializers.ValidationError("User Must be authenticated to make an appointment")
            return value
        
        def validate(self, data):
            patient = data['user']
            program = data['program']

            if not program.programs.filter(patient=patient).exists():
                raise serializers.ValidationError(f"Patient {patient.username} is not enrolled in this program.")
            
            return data