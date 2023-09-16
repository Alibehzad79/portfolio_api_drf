from rest_framework import serializers
from account_app.models import Profile, CustomerFeadback, Email, MyWorkExperience, Project, Service, Social

class CustomerFeadbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeadback
        fields = '__all__'
        
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
        
class MyWorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWorkExperience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        


class ProfileSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    feadbacks = serializers.SerializerMethodField()
    experiances = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    socials = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = '__all__'   
        
    def get_projects(self, obj):
        return [ProjectSerializer(s).data for s in obj.projects.all()]
    def get_feadbacks(self, obj):
        return [CustomerFeadbackSerializer(s).data for s in obj.customerfeadback.all()]
    def get_experiances(self, obj):
        return [MyWorkExperienceSerializer(s).data for s in obj.myworkexperience.all()]
    def get_services(self, obj):
        return [ServiceSerializer(s).data for s in obj.services.all()]        
    def get_socials(self, obj):
        return [SocialSerializer(s).data for s in obj.socials.all()]    