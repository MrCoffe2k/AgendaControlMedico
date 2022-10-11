from django.contrib.auth.forms import UserCreationForm  #importa la plantilla del formulario generico de python
from django.contrib.auth.models import User #importa el modelo por defecto del usuario
from django import forms
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']