from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

def busquedaProductos(request):

    return render(request, "busquedaProductos.html")

def buscar(request):

    if(request.GET["producto"]):
        #mensaje ="Artículo buscado: %r" %request.GET["producto"]
        producto = request.GET["producto"]

        if(len(producto) > 20):
            mensaje = "Texto de búsqueda demasiado largo"

        else:

            articulos = Articulos.objects.filter(nombre__icontains = producto)

            return render(request, "resultadosBusqueda.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = "No has introducido nada"
    

    return HttpResponse(mensaje)


def contacto(request):

    if(request.method == "POST"):
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["lucasdeferrari03@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")


    return render(request, "contacto.html")


def contacto2(request):
    
        if(request.method == "POST"):
            miFormulario = FormularioContacto(request.POST)
    
            if(miFormulario.is_valid()):
                infForm = miFormulario.cleaned_data
    
                send_mail(infForm["asunto"], infForm["mensaje"],
                infForm.get("email", "lucasdeferrari03@gmail.com"), ["lucasdeferrari03@gmail.com"],)

                return render(request, "gracias.html")
            
            else:
                return HttpResponse("El formulario no es válido")
            
        else:
            miFormulario = FormularioContacto() #para que se muestre el formulario vacio

        return render(request, "formulario_contacto2.html", {"form": miFormulario})

