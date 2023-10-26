from django.contrib import admin
from .models import CategoriaProd, Producto


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'precio', 'disponible')
    search_fields = ('nombre', 'categorias__nombre')
    list_filter = ('disponible', 'categorias__nombre')


admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)