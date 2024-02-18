from django.shortcuts import render

from rest_framework import generics
from .models import Student
# import .serializers
from .serializers import *
# StudentSerializer, StudentByBnumberSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# views.py

class StudentByBnumberAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentByBnumberSerializer
    lookup_field = 'bnumber'

class StudentByEmailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentByEmailSerializer
    lookup_field = 'email'

class StudentByMajorAPIView(generics.ListAPIView):
    serializer_class = StudentByMajorSerializer

    def get_queryset(self):
        major = self.kwargs['major']
        return Student.objects.filter(major=major)
