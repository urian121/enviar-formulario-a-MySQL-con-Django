from django import forms


class EmpleadoForm(forms.Model):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50, required=False)
    edad = forms.IntegerField(max_length=2, required=True)
