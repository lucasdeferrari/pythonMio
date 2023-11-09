from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Las credenciales proporcionadas son incorrectas. Por favor, inténtalo de nuevo.',
        'inactive': 'Esta cuenta está inactiva. Por favor, contacta al administrador.',
    }
