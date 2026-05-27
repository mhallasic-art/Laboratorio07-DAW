from django import forms
from .models import NotaAlumnoPorCurso

class NotaForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields = '__all__'