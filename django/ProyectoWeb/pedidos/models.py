from django.db import models
from django.contrib.auth.models import User
from tienda.models import Producto


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
       
        return self.lineapedido_set.aggregate(
            total=models.Sum(
                models.F('producto_id__precio') * models.F('cantidad'),
                output_field=models.FloatField()
            )
        )['total']
       


    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}' 
    
    class Meta:
        db_table = 'lineaPedidos'
        verbose_name = 'linea de pedido'
        verbose_name_plural = 'lineas de pedidos'
        ordering = ['id']