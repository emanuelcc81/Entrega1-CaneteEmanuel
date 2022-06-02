from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.inicio),
    path("productos" , views.productos, name="productos"),
    path("alta_productos" , views.productos_formulario),
    path("buscar_producto" , views.buscar_producto),
    path("resultado_busqueda" , views.resultado_productos),
    path("datos" , views.datos, name="datos"),
    path("alta_datos" , views.datos_formulario),
    path("proveedores" , views.proveedores, name="proveedores"),
    path("alta_proveedores" , views.proveedores_formulario)

]