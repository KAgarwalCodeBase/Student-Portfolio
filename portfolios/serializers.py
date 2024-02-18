from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# serializers.py

class StudentByBnumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['bnumber', 'name', 'email', 'major']

class StudentByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['bnumber', 'name', 'email', 'major']

class StudentByMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['bnumber', 'name', 'email', 'major']
