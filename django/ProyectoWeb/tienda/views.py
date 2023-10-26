from django.shortcuts import render
from .models import CategoriaProd, Producto

def tienda(request):

    productos = Producto.objects.all()
        
    return render(request, "tienda/tienda.html", {'productos':productos})
