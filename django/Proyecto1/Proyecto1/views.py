from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

class Persona(object):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


def saludo(request): # primera vista 
    cadena = """ <html>
    <body>
    <h1>
    Hola crack 
    </h1>
    </body>
    </html>
""" #puedo usar html para modificar la cadena a mi gusto NO RECOMENDADO HACER ACA

    return HttpResponse(cadena)  

def despedida(request):
    return HttpResponse("Chau crack")

def dameFecha(request):
    fechaActual = datetime.datetime.now()

    fechaYHoraActual = """ <html>
    <body>
    <h2>
    Fecha y hora actuales %s 
    </h2>
    </body>
    </html>
""" % fechaActual
    
    return HttpResponse(fechaYHoraActual)

def calculaEdad(request,edad,anio):
    periodo = anio-2023
    edadFutura = edad + periodo

    cadena = """ <html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>
""" % (anio, edadFutura) # NO RECOMENDADO USAR HTML DIRECTO, USAR PLANTILLAS
    
    return HttpResponse(cadena)

def saludoConPlantilla(request): 

    docExterno = open("C:/Users/Lucas/OneDrive - UTN.BA/Documentos/pythonMio/django/Proyecto1/Proyecto1/plantillas/miPlantilla.html")
    plantilla = Template(docExterno.read())

    docExterno.close()
    contexto = Context()
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def saludoConVariable(request):
    nombre = "Lucas"
    apellido = "Deferrari"
    fechaHoraActual = datetime.datetime.now()
    
    docExterno = open("C:/Users/Lucas/OneDrive - UTN.BA/Documentos/pythonMio/django/Proyecto1/Proyecto1/plantillas/saludoConVariable.html")
    plantilla = Template(docExterno.read())

    docExterno.close()
    contexto = Context({"nombrePersona":nombre, "apellidoPersona": apellido, "momentoActual" : fechaHoraActual}) #se puede usar para almacenar variables, objetos
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def saludoConObjetos(request):
    persona1 = Persona("Lucas", "Deferrari", 20)
    temasDelCurso = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]

    fechaHoraActual = datetime.datetime.now()
    
    docExterno = open("C:/Users/Lucas/OneDrive - UTN.BA/Documentos/pythonMio/django/Proyecto1/Proyecto1/plantillas/saludoConObjetos.html")
    plantilla = Template(docExterno.read())

    docExterno.close()
    contexto = Context({"nombrePersona":persona1.nombre, "apellidoPersona": persona1.apellido, "edadPersona": persona1.edad, "temas": temasDelCurso, "momentoActual" : fechaHoraActual})
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def clase8(request):
    paises = ["Holanda", "Oman", "Lituania", "Argentina"]

    fechaHoraActual = datetime.datetime.now()
    
    # GUARDE LAS PLANTILLAS EN settings.py
    docExterno = loader.get_template('clase8.html')

    # Puedo renderizar el documento directamente si lo hago con loader, no tengo q usar el contexto
    documento = docExterno.render({"paises": paises, "momentoActual" : fechaHoraActual})

    return HttpResponse(documento)

