from django.shortcuts import render
from .models import Project
from rest_framework import viewsets
from .serializers import ProjectSerializer

# Create your views here.

class ProjectsViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):

        projects = Project.objects.all()

        name = self.request.GET.get('name')

        if name:

            projects = projects.filter(nombre__contains=name)

        else:

            return projects