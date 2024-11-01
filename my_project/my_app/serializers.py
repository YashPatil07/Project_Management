#serializers.py
# complex data(quertset and model instances) ->convert into -> native python datatypes so that it cant be easily render into JSON
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']
