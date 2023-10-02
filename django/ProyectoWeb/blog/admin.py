from django.contrib import admin
from .models import Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # list_display = ('titulo', 'autor', 'created')
    # ordering = ('autor', 'created')
    # search_fields = ('titulo', 'autor__username', 'categoria__nombre')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
