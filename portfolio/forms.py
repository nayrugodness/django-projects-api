from django import forms
from .models import Project, Language, Framework, Library


class ProjectForms(forms.ModelForm):

    class Meta:

        model = Project
        fields = '__all__'


class LanguageForms(forms.ModelForm):

    class Meta:

        model = Language
        fields = '__all__'


class FrameworkForms(forms.ModelForm):

    class Meta:

        model = Framework
        fields = '__all__'

class LibraryForms(forms.ModelForm):

    class Meta:

        model = Library
        fields = '__all__'