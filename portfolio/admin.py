from django.contrib import admin
from .models import Project, Language, Framework
from .forms import ProjectForms, LanguageForms, FrameworkForms

class ProjectAdmin(admin.ModelAdmin):

    form = ProjectForms

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Framework)