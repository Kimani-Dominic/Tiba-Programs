from rest_framework import serializers

from appointments.models import Appointment
from .models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = MedicalRecord
        fields = ['id','appointment', 'program', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['patient', 'appointment', 'program', 'created_at', 'updated_at']
        
        
    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("User Must be authenticated")
        return value
            
    def validate_appointment(self, value):
        if not Appointment.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Appointment does not exist.")
        return value
    
    def create(self, validated_data):
        appointment = validated_data['appointment']
        validated_data['patient'] = appointment.user 
        validated_data['program'] = appointment.program  
        
        return super().create(validated_data)
    
   