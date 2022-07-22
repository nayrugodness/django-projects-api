from django.db.models.query import QuerySet
from .models import Project, Language, Framework
from rest_framework import fields, serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'