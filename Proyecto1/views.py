from django.http import HttpResponse
import datetime     

def saludo(request):
    return HttpResponse('hola esta clase es horrible') #Primero el mensaje que vamos a mostrar


def segunda_vista(request):
    return HttpResponse('Alta claseeee papá')

def dia_actual(request):
    dia = datetime.datetime.now()
    return HttpResponse(f'La fecha actual es {dia}')

def saludo_personalizado(request, nombre):          #Pide un parametro
    return HttpResponse(f'Hola {nombre}')
