from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


class RegistroUsuarioView(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return redirect('Home')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, 'registro/registro.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect('Home')
    
def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)

            return redirect('Home')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, "login/iniciar_sesion.html", {"form":form})
    
    else:
        form = AuthenticationForm()

        return render(request, "login/iniciar_sesion.html", {"form":form})
