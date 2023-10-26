from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio

def home(request):

    return render(request, "ProyectoWebApp/home.html")


