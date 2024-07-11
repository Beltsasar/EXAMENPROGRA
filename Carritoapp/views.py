from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import JsonResponse
from .models import Comentario

from .models import Usuario, Comentario

def Registro(request):

    return render(request,'Registro.html/')



def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['login']
        clave = request.POST['clave']
        nombre_completo = request.POST['nombre']
        telefono = request.POST['fono']
        correo = request.POST['email']
        comuna = request.POST['comuna']
        edad = request.POST['edad']

        usuario = Usuario(nombre=nombre, clave=clave, nombre_completo=nombre_completo, telefono=telefono,
                          correo=correo, comuna=comuna, edad=edad)
        usuario.save()
        return redirect('registro_exitoso')  # Puedes definir una página de éxito de registro

    return render(request, 'tu_app/registro.html')  # Asegúrate de ajustar la ruta a tu plantilla



def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


@login_required

def eliminar_usuario(request):
    if request.method == 'POST':
        clave = request.POST['clave']
        # Verificar la clave actual del usuario
        usuario = AuthenticationError(username=request.user.username, password=clave)
        if usuario is not None:
            # Clave válida, eliminar el usuario
            request.user.delete()
            messages.success(request, 'Tu cuenta ha sido eliminada correctamente.')
            return redirect('pagina_principal')  # Redirigir a la página principal u otra vista después de eliminar
        else:
            messages.error(request, 'La clave ingresada no es válida. Inténtalo nuevamente.')
            return render(request, 'eliminar_usuario.html')
    else:
        return render(request, 'eliminar_usuario.html')

def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'user_list.html', {'users': users})
    
def eliminar_usuario(request):
    users = Usuario.objects.all()

    
    return render(request,'eliminar_usuario.html',{'users': users})

def mostrarIndex(request):
    
    return render(request,'inicio.html')


def mostrarIndex(request):
    return render(request, 'inicio.html')

def seccion_frutas(request):
    return render(request, 'frutas.html')

def seccion_yoghurt(request):
    return render(request, 'Yoghurt.html')

def seccion_Quesos(request):
    return render(request, 'quesos.html')

def seccion_leche(request):
    return render(request, 'leche.html')

def seccion_Postres(request):
    return render(request, 'Postres.html')

def seccion_congelados(request):
    return render(request, 'Congelados.html')


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        clave = request.POST['clave']

        try:
            usuario = Usuario.objects.get(nombre=nombre, clave=clave)
            request.session['usuario_id'] = usuario.id
            return redirect('dashboard')
        except Usuario.DoesNotExist:
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def eliminar_usuario(request, usuario_id=None):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, id=usuario_id)
        usuario.delete()
        # Después de eliminar, redirige a la lista de usuarios
        return redirect('user_list')  # Ajusta 'user_list' al nombre correcto de tu vista de lista de usuarios
    
    # Si la solicitud no es POST, obtén y muestra la lista de usuarios
    usuarios = Usuario.objects.all()
    return render(request, 'eliminar_usuario.html', {'usuarios': usuarios})

def dashboard(request):
    return render(request, 'dashboard.html')




def contacto_view(request):
    return render(request, 'contacto.html')

def enviar_comentario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')
        mensaje = request.POST.get('mensaje', '')

        # Validación básica de campos
        if not nombre or not email or not mensaje:
            return JsonResponse({'status': 'error', 'message': 'Por favor, completa todos los campos obligatorios.'})

        # Validar que el correo electrónico no esté duplicado en la base de datos
        if Comentario.objects.filter(Q(email=email)).exists():
            return JsonResponse({'status': 'error', 'message': 'Ya existe un comentario registrado con este correo electrónico.'})

        # Guardar el comentario en la base de datos
        comentario = Comentario.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            mensaje=mensaje,
        )

        # Respuesta de éxito
        return JsonResponse({'status': 'success', 'message': '¡Gracias por tu comentario! Nos pondremos en contacto contigo pronto.'})

    # Redirigir a la página principal si no es POST
    return HttpResponseRedirect('/')

def VerCarro(request):
    
    return render(request,'Carrito.html')