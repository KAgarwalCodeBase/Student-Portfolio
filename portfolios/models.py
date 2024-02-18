from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Student(models.Model):
    bnumber = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    major = models.CharField(max_length=10)
    admission_year =  models.IntegerField(('year'), choices=year_choices, default=current_year)
    current_gpa = models.FloatField(null=True)
    mobile_number =  PhoneNumberField()
    address = models.CharField(max_length=200, null=True)
    linkedin_url =models.URLField(max_length = 200, null=True) 
    github_url = models.URLField(max_length = 200, null=True) 

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.project_title


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    description = models.TextField()
    course = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField() 

class WorkExperience(models.Model):
    start_year = models.IntegerField(('year'), choices=year_choices, default=current_year)
    end_year = models.IntegerField(('year'), choices=year_choices, default=current_year)

