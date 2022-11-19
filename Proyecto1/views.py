from django.http import HttpResponse
from django.shortcuts import render
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

def mostrar_html (request):                         #Aquí ya utilizamos RENDER para tomar los datos del HTML. Va a renderizar el HTML
    return render(request, 'hola.html')

def segundo_html (request):
    return render(request, 'otro.html', {'nombre':'Juan Manuel', 'lista':[1,2,3,4,5]})       #Agregué como segundo parámetro un DICCIONARIO

def guia_render_html (request):
    return render(request, 'guia.html')