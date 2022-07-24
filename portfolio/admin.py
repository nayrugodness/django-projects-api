from django.contrib import admin
from .models import Project, Language, Framework, Library
from .forms import ProjectForms, LanguageForms, FrameworkForms, LibraryForms

class ProjectAdmin(admin.ModelAdmin):

    form = ProjectForms

class LanguageAdmin(admin.ModelAdmin):

    form = LanguageForms

class FrameworkAdmin(admin.ModelAdmin):

    form = FrameworkForms

class LibraryAdmin(admin.ModelAdmin):

    form = LibraryForms

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Library, LibraryAdmin)