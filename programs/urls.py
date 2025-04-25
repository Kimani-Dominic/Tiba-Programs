from django.urls import path
from .views import *

urlpatterns = [
    path('api/programs/create/', HealthProgramCreateView.as_view(), name='create-record'),
    path('api/programs/', PatientHealthRecordListView.as_view(), name='list-records'),
    path('api/programs/patient-enrollment/',ProgramEnrollmentListCreateView.as_view(), name='enroll-patient' )
    
]
