from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
import datetime
from django.utils.translation import gettext_lazy as _

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]

def current_year():
    return datetime.date.today().year

class ChoicesMixin:
    @classmethod
    def get_choices(cls):
        return [(choice, choice) for choice in cls.CHOICES]

class ExpertiseArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default="description")
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BNumberField(models.CharField):
    description = _("BNumber")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 10)
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value and not value.startswith('B'):
            return f'B{value}'
        return value


class Student(models.Model):
    bnumber = BNumberField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    graduated = models.BooleanField(default=False)
    major = models.CharField(max_length=10)
    admission_year = models.IntegerField('year', choices=year_choices, default=current_year)
    current_gpa = models.FloatField(null=True)
    mobile_number = PhoneNumberField()
    address = models.CharField(max_length=200, null=True)
    linkedin_url = models.URLField(max_length=200, null=True)
    github_url = models.URLField(max_length=200, null=True)
    preferred_roles = models.ManyToManyField(Role, related_name='preferred_students')
    current_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='current_students', default=None)
    expertise_areas = models.ManyToManyField(ExpertiseArea)
    image_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='portfolio')
    description = models.TextField()

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_url = models.URLField(max_length=200, null=True)

    class Meta:
        ordering = ['-start_date']

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)  # Reverting to ForeignKey
    start_year = models.IntegerField('year', choices=year_choices, default=current_year)
    end_year = models.IntegerField('year', choices=year_choices, default=current_year, null=True)
    ongoing = models.BooleanField(default=False)


    class Meta:
        ordering = ['-start_year']

class Education(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='educations')
    ongoing = models.BooleanField(default=False)
    degree_name = models.CharField(max_length=200)
    start_year = models.IntegerField('year', choices=year_choices, default=current_year)
    end_year = models.IntegerField('year', choices=year_choices, default=current_year, null=True)
    university = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-start_year']
