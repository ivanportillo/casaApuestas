from django.contrib import admin
from apuestas.models import perfilUsuario, Deporte, Apuesta, Participacion

admin.site.register(perfilUsuario)
admin.site.register(Deporte)
admin.site.register(Apuesta)
admin.site.register(Participacion)
