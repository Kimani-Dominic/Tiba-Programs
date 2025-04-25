from rest_framework import serializers

from programs.models import *
        
        
class HealthProgramSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']
 
        
        def validate_user(self, value):
            if not value:
                raise serializers.ValidationError("User Must be authenticated")
            return value
        
class ProgramEnrollmentSerializer(serializers.ModelSerializer):
    program = HealthProgramSerializer(read_only=True)
    program_id = serializers.PrimaryKeyRelatedField(
        queryset=HealthProgram.objects.all(),
        source='program',
        write_only=True
    )
    doctor = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_doctor=True))
    patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_patient=True))

    class Meta:
        model = ProgramEnrollment
        fields = ['id', 'doctor', 'patient', 'program', 'program_id', 'enrolled_on']
        
        def enroll_patient(self, validated_data):
            program = validated_data.pop('program')
            enrollment = ProgramEnrollment.objects.create(**validated_data)
            
            return enrollment
        