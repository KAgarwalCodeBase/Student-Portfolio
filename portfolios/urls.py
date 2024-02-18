from django.urls import path
from .views import *

urlpatterns = [
    path('api/students/', StudentListAPIView.as_view(), name='student-list'),
    path('api/students/bnumber/<str:bnumber>/', StudentByBnumberAPIView.as_view(), name='student-by-bnumber'),
    path('api/students/email/<str:email>/', StudentByEmailAPIView.as_view(), name='student-by-email'),
    path('api/students/major/<str:major>/', StudentByMajorAPIView.as_view(), name='student-by-major'),
    
    # Add other URL patterns as needed
]
