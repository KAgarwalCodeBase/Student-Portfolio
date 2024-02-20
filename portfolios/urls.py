from django.urls import path
from .views import *

urlpatterns = [
    path('api/students/', StudentListAPIView.as_view(), name='student-list'),
    path('api/students/bnumber/<str:bnumber>/', StudentByBnumberAPIView.as_view(), name='student-by-bnumber'),
    path('api/students/email/<str:email>/', StudentByEmailAPIView.as_view(), name='student-by-email'),
    path('api/students/major/<str:major>/', StudentByMajorAPIView.as_view(), name='student-by-major'),
    # path('my-view/', my_view, name='my-view'),  # Add this URL pattern
    path('portfolio/<str:bnumber>/', my_view, name='my_view'),

    path('students/bnumber/<str:bnumber>/', StudentDetailByBnumberAPIView.as_view(), name='student-detail-by-bnumber'), 
    path('send-email/', send_email_view, name='send_email'),
    # Add other URL patterns as needed
]
