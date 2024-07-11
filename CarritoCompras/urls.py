"""
URL configuration for CarritoCompras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Carritoapp.views import VerCarro,enviar_comentario,contacto_view,Registro,login_view,dashboard,eliminar_usuario, registro_usuario,registro_exitoso,mostrarIndex,user_list,seccion_frutas, seccion_yoghurt, seccion_Quesos, seccion_leche, seccion_Postres, seccion_congelados


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrarse/',Registro,name='Registro'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('registro_exitoso/', registro_exitoso, name='registro_exitoso'),
    path('inicioSMK/', mostrarIndex, name='mostrarIndex'),
    path('frutas/', seccion_frutas, name='seccion_frutas'),
    path('Yoghurt/', seccion_yoghurt, name='seccion_yoghurt'),
    path('Quesos//', seccion_Quesos, name='seccion_Quesos'),
    path('Leches/', seccion_leche, name='seccion_leche'),
    path('Postres/', seccion_Postres, name='seccion_Postres'),
    path('congelados/', seccion_congelados, name='seccion_congelados'),
    path('usuarios/', user_list, name='user_list'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('eliminar_usuario/',eliminar_usuario,name='EliminarUser'),
    path('eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),  # Ruta para eliminar usuario
    path('contacto/', contacto_view, name='contacto'),
    path('enviar_comentario/', enviar_comentario, name='enviar_comentario'),
    path('VerCarro/', VerCarro, name='VerCarro'),


]
