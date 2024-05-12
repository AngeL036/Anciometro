import random
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import depresion,ansiedad

# Create your views here.
def IndexView(request):
    return render(request,'paginaPrincipal.html')

def Ansiedad(request):
    return render(request,'test_ansiedad.html')

def DepresionView(request):
    return render(request,'test_depresion.html')

def estadisticas(request):
    return render(request,'estadisticas.html')

def seguimiento(request):
    formularioD = depresion.objects.latest('fecha')
    formularioA = ansiedad.objects.latest('fecha')
    depresionR = porcentaje(formularioD.respuestas)
    ansiedadR = porcentaje(formularioA.respuestas)
    context = {
        'depresion' : depresionR,
        'ansiedad'  : ansiedadR,

    }
    return render(request,'seguimiento_progreso.html',context)
def porcentaje(respuestas):
    porcentaje = 0
    for letra in respuestas:
        if letra == '1':
            porcentaje += 1
    return round((porcentaje*100)/12)
@login_required
def respuestas1(request):
    if request.method == 'POST':
        respuesta = ''.join([request.POST.get(f'pregunta{i}') for i in range(1,13)])
        respuestas = str(respuesta)
        fecha = datetime.now()
        nombres = request.user
        nueva_depresion = depresion(
            respuestas = respuestas,
            fecha = fecha,
            nombreUser = nombres,
            comentario = ''
            
        )
        nueva_depresion.save()

        return redirect('aplicacion:IndexView')
        #return HttpResponse("¡Formulario enviado correctamente!")
    else:
        return HttpResponse("El formulario solo puede ser enviado mediante una solicitud POST.")

@login_required
def respuesta2(request):
    if request.method == 'POST':
        respuestas = ''.join([request.POST.get(f'pregunta{i}') for i in range(1,13)])
        fecha = datetime.now()
        nombre = request.user
        nueva_ansiedad = ansiedad(
            respuestas = respuestas,
            fecha = fecha,
            nombreUser = nombre

        )
        nueva_ansiedad.save()
        return redirect('aplicacion:IndexView')
    else:
        return HttpResponse("El formulario solo puede ser enviado mediante una solicitud POST.")
        