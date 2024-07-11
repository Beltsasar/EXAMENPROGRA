from django.contrib import admin
from .models import Usuario,Comentario  # Asegúrate de importar tu modelo de usuario correctamente

admin.site.register(Usuario)

admin.site.register(Comentario)

