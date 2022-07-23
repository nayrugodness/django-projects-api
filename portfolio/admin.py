from django.contrib import admin
from .models import Project, Language, Framework
from .forms import ProjectForms, LanguageForms, FrameworkForms

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Framework)