from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio
from carroCompras.carro import Carro

def home(request):
    carro = Carro(request)

    return render(request, "ProyectoWebApp/home.html")


