from django.contrib import admin
from .models import Project, Language, Framework
from .forms import ProjectForms, LanguageForms, FrameworkForms

class ProjectAdmin(admin.ModelAdmin):

    form = ProjectForms

class LanguageAdmin(admin.ModelAdmin):

    form = LanguageForms

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework)