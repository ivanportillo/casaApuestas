from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import perfilUsuario
from django.contrib.auth.models import User
from datetime import timedelta, date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class registroForm(UserCreationForm):
    username = forms.CharField(required=True, label = "Nombre de usuario")
    fecha_nacimiento = forms.DateField(required=True, label="Fecha de nacimiento")
    email = forms.EmailField(required=True, label = "Correo electronico")
    first_name = forms.CharField(required=True, label = "Nombre")
    last_name = forms.CharField(required=True, label = "Apellidos")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "fecha_nacimiento")

    def save(self, commit=True):
        user = super(registroForm, self).save(commit)
        datos = self.cleaned_data
        usuario = perfilUsuario.objects.create(usuario = user, fechaNacimiento=datos['fecha_nacimiento'])
        return usuario

    def clean_fecha_nacimiento(self):
        fecha_nacimiento_valid = self.cleaned_data['fecha_nacimiento']
        fecha_nacimiento_valid=(fecha_nacimiento_valid+timedelta(days=6574))
        if fecha_nacimiento_valid >= date.today():
            raise ValidationError("El usuario debe ser mayor de edad.")
        return self.cleaned_data['fecha_nacimiento']
