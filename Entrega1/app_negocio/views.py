import re
from django.http import HttpResponse
from django.shortcuts import render
from app_negocio.models import Productos
from app_negocio.models import Datos_productos
from app_negocio.models import Proveedores
from django.template import loader
from app_negocio.forms import Productos_formulario
from app_negocio.forms import Datos_formulario
from app_negocio.forms import Proveedores_formulario
import datetime

# Create your views here.
def inicio(request):

    return render ( request, "padre.html")


def productos(request):
    producto = Productos.objects.all()
    dicc = {"producto" : producto}
    plantilla = loader.get_template("productos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alta_productos(request, nombre):
    producto = Productos(nombre=nombre , precio=200)
    producto.save()
    texto = f"Se guardo el Producto: {producto.nombre} Precio: {producto.precio}"
    return HttpResponse(texto)


def productos_formulario(request):

    if request.method == "POST":

        mi_formulario = Productos_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            producto = Productos( nombre=datos['nombre'] , precio=datos['precio'])
            producto.save()

            return render( request , "formulario_productos.html")

    return render( request, "formulario_productos.html")


def buscar_producto(request):

    return render( request , "buscar_productos.html")


def resultado_productos(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        producto = Productos.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_productos.html" , {"productos": producto})
    else:
        return HttpResponse("Campo vacio")
 

def datos(request):
    datos = Datos_productos.objects.all()
    dicc = {"datos" : datos}
    plantilla = loader.get_template("datos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento ) 


def datos_formulario(request):

    if request.method == "POST":

        mi_formulario = Datos_formulario( request.POST )

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data          
            
            datos = Datos_productos( nombre=info['nombre'] , marca=info['marca'], fecha_fab=info['fecha_fab'])
            datos.save()

            return render( request , "formulario_datos.html")

    return render( request, "formulario_datos.html")


def proveedores(request):
    proveedores = Proveedores.objects.all()
    dicc = {"proveedores" : proveedores}
    plantilla = loader.get_template("proveedores.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento ) 


def proveedores_formulario(request):

    if request.method == "POST":

        mi_formulario = Proveedores_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            proveedores = Proveedores( nombre=datos['nombre'] , telefono=datos['telefono'])
            proveedores.save()

            return render( request , "formulario_proveedores.html")

    return render( request, "formulario_proveedores.html")


