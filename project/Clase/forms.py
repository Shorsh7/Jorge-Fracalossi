from django import forms

from . import models

class ComisionForm(forms.ModelForm):
    class Meta:
        model = models.Comision
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = '__all__'