from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carroCompras.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="autenticacion/iniciar_sesion")
def procesarPedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            user = request.user,
            producto_id = key,
            pedido_id = pedido.id,
            cantidad = value["cantidad"],
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_email(pedido.id, lineas_pedido, usuario = request.user, email = request.user.email)
    
    carro.limpiar_carro()
    messages.success(request, f'Pedido No. {pedido.id} creado exitosamente')

    return redirect('Tienda')


def enviar_email(pedido, lineas_pedido, usuario, email):
    asunto = f'Pedido No. {pedido} fue recibido correctamente.'
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "usuario": usuario,
        "email": email,
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "lucasdeferrari03@gmail.com"
    to_email = email

    send_mail(asunto, mensaje_texto, from_email, [to_email], html_message=mensaje)