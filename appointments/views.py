# views.py
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import generics, permissions

from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        # if not user.groups.filter(name='doctor').exists():
        #     raise PermissionError("Only doctors can create appointments.")
        
        serializer.save()


class AppointmentListView(ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateAppointmentStatusView(RetrieveUpdateAPIView):
  
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def update(self, request, *args, **kwargs):
        appointment = self.get_object()
        
        status = request.data.get('status')
        if status not in dict(Appointment.STATUS_CHOICES):
            return Response({"error": "Invalid status."}, status.HTTP_400_BAD_REQUEST)
        
        appointment.status = status
        appointment.save()
        
        return Response(AppointmentSerializer(appointment).data, status.HTTP_200_OK)
