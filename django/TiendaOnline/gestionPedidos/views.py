from django.shortcuts import render
from django.http import HttpResponse

def busquedaProductos(request):

    return render(request, "busquedaProductos.html")

def buscar(request):
    mensaje ="Artículo buscado: %r" %request.GET["producto"]

    return HttpResponse(mensaje)
