from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    # AGREGO ESOS CAMPOS PARA PERMITIR QUE EL MAIL NO SEA OBLIGATORIO
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return 'Cliente: %s' %(self.nombre)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    #ESE CAMPO SIRVE PARA CAMBIAR EL NOMBRE QUE SE MUESTRA EN EL PANEL DE ADMINISTRACION
    seccion=models.CharField(max_length=20, verbose_name= "Seccion del artículo")
    precio=models.IntegerField()

    def __str__(self):
        return 'Nombre: %s Seccion: %s Precio: %s' %(self.nombre, self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return 'Numero: %s' %(self.numero)

