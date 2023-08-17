from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    comision = forms.IntegerField(required=True)
    