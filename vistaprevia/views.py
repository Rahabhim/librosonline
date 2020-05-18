from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

# def index(request):
#     return HttpResponse("Hola Maxi!")

def index(request):
    contenido = { 'nombre_sitio': 'LibrosOnline' }
    return render(request, 'vistaprevia/index.html', contenido)
