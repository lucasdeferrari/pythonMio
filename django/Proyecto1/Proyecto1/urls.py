"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad, saludoConPlantilla, saludoConVariable, saludoConObjetos, clase8, shortcuts, pressBancaHerencia, sentadillaHerencia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), # NO TIENE NADA QUE VER EL NOMBRE DE LA VISTA CON EL DE LA URL
    path('despedida/', despedida),
    path('fechaHora/' , dameFecha),
    path('edad/<int:edad>/<int:anio>', calculaEdad),
    path('saludoPlt/', saludoConPlantilla),
    path('saludoVar/', saludoConVariable),
    path('saludoObj/', saludoConObjetos),
    path('clase8/', clase8),
    path('shortcuts/', shortcuts),
    path('pressBanca/', pressBancaHerencia),
    path('sentadilla/', sentadillaHerencia)
]
