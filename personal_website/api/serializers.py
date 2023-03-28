from rest_framework import serializers
from .models import About, CV, Project

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'