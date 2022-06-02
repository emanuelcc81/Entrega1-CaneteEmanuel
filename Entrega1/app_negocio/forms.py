from django import forms


class Productos_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()

class Datos_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    fecha_fab = forms.DateField()

class Proveedores_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()