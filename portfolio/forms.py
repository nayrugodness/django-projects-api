from django import forms
from .models import Project, Language, Framework


class ProjectForms(forms.ModelForm):

    class Meta:

        model = Project
        fields = '__all__'


class LanguageForms(forms.ModelForm):

    class Meta:

        model = Language
        fields = '__all__'