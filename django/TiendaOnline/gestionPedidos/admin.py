from django.contrib import admin
from gestionPedidos.models import Articulos, Clientes, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion")
    search_fields = ("nombre", "seccion")
    list_filter = ("seccion", )

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos, PedidosAdmin)

