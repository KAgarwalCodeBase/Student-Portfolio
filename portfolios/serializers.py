from rest_framework import serializers
from .models import Student, Portfolio, Project, WorkExperience, Education, Role, ExpertiseArea

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


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()

    class Meta:
        model = WorkExperience
        fields = ['role_name', 'company_name', 'description', 'country', 'start_year', 'end_year', 'ongoing']

    def get_role_name(self, obj):
        return obj.role.name  # Fetch the name of the related role

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']


class ExpertiseAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertiseArea
        fields = '__all__'



class StudentDetailSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer()
    projects = ProjectSerializer(many=True)
    work_experiences = WorkExperienceSerializer(many=True)
    educations = EducationSerializer(many=True)
    preferred_role_names = serializers.SerializerMethodField()
    current_role_name = serializers.SerializerMethodField()
    # expertise_area_names = serializers.SerializerMethodField()
    expertise_areas = ExpertiseAreaSerializer(many=True)


    class Meta:
        model = Student
        fields = ['bnumber', 'image_url', 'name', 'email', 'graduated', 'major', 'admission_year', 'current_gpa',
                  'mobile_number', 'address','current_role_name', 'linkedin_url', 'github_url', 'preferred_role_names', 'expertise_areas',
                  'portfolio', 'projects', 'work_experiences', 'educations']
    
    def get_preferred_role_names(self, obj):
        return [role.name for role in obj.preferred_roles.all()]
    
    # def get_expertise_area_names(self, obj):
    #     return [expertise_area.name for expertise_area in obj.expertise_areas.all()]
    
    def get_expertise_areas(self, obj):
        expertise_areas = obj.expertise_areas.all()
        return ExpertiseAreaSerializer(expertise_areas, many=True).data
    def get_current_role_name(self, obj):
        return obj.current_role.name
    
    