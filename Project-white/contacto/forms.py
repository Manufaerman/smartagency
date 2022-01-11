from django import forms

class Formcontacto(forms.Form):
    nombre = forms.CharField(label='nombre',required=True ,max_length=100)
    Email = forms.CharField(label='Email',required=True ,max_length=100)
    contenido = forms.CharField(label='contenido',widget=forms.Textarea)