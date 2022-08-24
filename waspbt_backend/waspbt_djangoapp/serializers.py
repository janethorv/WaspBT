from rest_framework import serializers
from .models import Project, Issue

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'participants',
            'admins',
            'date',
            'get_absolute_url'
        )
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = (
            'id',
            'project',
            'slug',
            'title',
            'author',
            'description',
            'date',
            'priority',
            'state',
            'get_absolute_url'
            
        )