from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from .models import Apuesta, perfilUsuario, Deporte, Participacion
from forms import registroForm
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

ultimasApuestas = Apuesta.objects.order_by('fechaFin')[:5];
deportes = Deporte.objects.all();
context = { 'ultimasApuestas' : ultimasApuestas,
            'deportes' : deportes }

def index(request):
    ultimasApuestas = Apuesta.objects.order_by('fechaFin')[:5];
    context['ultimasApuestas'] = ultimasApuestas
    if request.user.is_authenticated():
        usuario = perfilUsuario.objects.get(usuario=request.user)
        context['usuario'] = usuario

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(username=usuario, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context['usuario'] = perfilUsuario.objects.get(usuario=request.user)
            else:
                context['mensaje'] = 'Cuenta no activa.'
                context['tipoMensaje'] = 2
                return render_to_response('apuestas/salir.html', context, RequestContext(request))
        else:
            context['mensaje'] = 'Nombre de usuario y/o password incorrectos.'
            context['tipoMensaje'] = 2
            return render_to_response('apuestas/salir.html', context, RequestContext(request))
    return render_to_response('apuestas/index.html', context, RequestContext(request))

def salir(request):
    if request.user.is_authenticated():
        logout(request)
        context['mensaje'] = 'Has cerrado sesion correctamente'
        context['tipoMensaje'] = 1
    else:
        context['mensaje'] = 'No tienes ninguna sesion iniciada'
        context['tipoMensaje'] = 2
    return render_to_response('apuestas/salir.html', context, RequestContext(request))

def registro(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = registroForm(request.POST)
            if form.is_valid():
                form.save()

                return HttpResponseRedirect('/')
        else:
            form = registroForm()

        context['form'] = form
        return render_to_response('apuestas/registro.html', context, RequestContext(request))
    else:
        context['mensaje'] = 'Ya tienes una sesion iniciada'
        context['tipoMensaje'] = 2
        return render_to_response('apuestas/salir.html', context, RequestContext(request))

def ingresar(request):
    if request.user.is_authenticated():
        usuario = perfilUsuario.objects.get(usuario=request.user)
        context['usuario'] = usuario
        if request.method == 'POST':
            dinero = request.POST.get('dinero')
            usuario = perfilUsuario.objects.get(usuario=request.user)
            usuario.dinero = float(dinero) + float(usuario.dinero)
            usuario.save()
            context['mensaje'] = 'Dinero ingresado correctamente'
            context['tipoMensaje'] = 1
            return render_to_response('apuestas/salir.html', context, RequestContext(request))
        else:
            return render_to_response('apuestas/ingresar.html', context, RequestContext(request))
    else:
        context['mensaje'] = 'Debes iniciar sesion para ingresar dinero'
        context['tipoMensaje'] = 2
        return render_to_response('apuestas/salir.html', context, RequestContext(request))

def perfil(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            email = request.POST.get('email')
            usuario = request.user
            usuario.first_name = nombre
            usuario.last_name = apellidos
            usuario.email = email
            usuario.save()
            context['mensaje'] = 'Perfil actualizado correctamente'
            context['tipoMensaje'] = 1
            return render_to_response('apuestas/salir.html', context, RequestContext(request))

        usuario = perfilUsuario.objects.get(usuario=request.user)
        context['usuario'] = usuario
        participaciones = Participacion.objects.filter(usuario=usuario)
        context['participaciones'] = participaciones
        return render_to_response('apuestas/perfil.html', context, RequestContext(request))
    else:
        context['mensaje'] = 'Debes iniciar sesion para ver tu perfil'
        context['tipoMensaje'] = 2
        return render_to_response('apuestas/salir.html', context, RequestContext(request))

def apuesta(request, idApuesta):
    if request.user.is_authenticated():
        apuesta = Apuesta.objects.get(id = idApuesta)
        if request.method == 'POST':
            opcion = request.POST.get('opcion')
            cantidad = request.POST.get('cantidad')
            usuario = perfilUsuario.objects.get(usuario=request.user)
            if float(cantidad) > float(usuario.dinero):
                context['mensaje'] = 'No tienes dinero suficiente para apostar'
                context['tipoMensaje'] = 2
                return render_to_response('apuestas/salir.html', context, RequestContext(request))
            cuotas = { '1' : apuesta.cuotaOpcion1,
                       '2' : apuesta.cuotaOpcion2,
                       '3' : apuesta.cuotaOpcion3
                     }
            cuota = cuotas[opcion]
            participacion = Participacion.objects.create(usuario = usuario, apuesta = apuesta, eleccion = opcion, cantidad = cantidad, cuotaEleccion = cuota)
            usuario.dinero = float(usuario.dinero) - float(cantidad)
            usuario.save()
            context['mensaje'] = 'Apuesta realizada correctamente'
            context['tipoMensaje'] = 1
            return render_to_response('apuestas/salir.html', context, RequestContext(request))
        context['apuesta'] = apuesta
        return render_to_response('apuestas/apuesta.html', context, RequestContext(request))
    else:
        context['mensaje'] = 'Debes iniciar sesion para apostar'
        context['tipoMensaje'] = 2
        return render_to_response('apuestas/salir.html', context, RequestContext(request))

def deporte(request, idDeporte):
    deporte = Deporte.objects.get(id = idDeporte)
    apuestasDeporte = Apuesta.objects.filter(deporte = deporte)
    context['deporte'] = deporte
    context['apuestas'] = apuestasDeporte
    return render_to_response('apuestas/deporte.html', context, RequestContext(request))

@staff_member_required
def resultados(request):
    if request.method == 'POST':
        idApuesta = request.POST.get('apuesta')
        resultado = request.POST.get('resultado')
        apuesta = Apuesta.objects.get(id = idApuesta)
        # apuesta.opcionGanadora = resultado
        # apuesta.save()

        participaciones = Participacion.objects.filter(apuesta = apuesta)
        for participacion in participaciones:
            print participacion.eleccion
            print resultado
            if int(participacion.eleccion) == int(resultado):
                participacion.usuario.dinero = float(participacion.usuario.dinero) + float(participacion.cantidad) * float(participacion.cuotaEleccion)
                participacion.usuario.save()
            participacion.delete()
        apuesta.delete()
    apuestas = Apuesta.objects.all()
    context['apuestas'] = apuestas

    return render_to_response('apuestas/resultados.html', context, RequestContext(request))
