from django.urls import path
from ProyectoWebApp import views
from .views import RegistroUsuarioView, cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('', RegistroUsuarioView.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="CerrarSesion"),
    path('iniciar_sesion', iniciar_sesion, name="IniciarSesion"),

]