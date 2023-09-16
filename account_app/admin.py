from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_app.models import CustomUser, Profile, Service, MyWorkExperience, Social, CustomerFeadback, Email, Project
from django.utils.translation import gettext_lazy as _

# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Project
    
class ServiceInline(admin.TabularInline):
    model = Service

class MyWorkExperienceInline(admin.TabularInline):
    model = MyWorkExperience

class SocialInline(admin.TabularInline):
    model = Social

class CustomerFeadbackInline(admin.TabularInline):
    model = CustomerFeadback



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    inlines = [
        ProjectInline,
        ServiceInline,
        MyWorkExperienceInline,
        SocialInline,
        CustomerFeadbackInline
    ]

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_sent')
    list_filter = ('date_sent',)
