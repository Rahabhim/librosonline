from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

# def index(request):
#     return HttpResponse("Hola Maxi!")

def index(request):
    contenido = { 'nombre_sitio': 'LibrosOnline' }
    para_minorista = { 'tipo_usuario' : 'minorista' , 'incremento' : '25'}
    para_mayorista = { 'tipo_usuario' : 'mayorista' , 'incremento' : '10'}
    # return render(request, 'vistaprevia/index.html', contenido)
    return render(request,
                'vistaprevia/index.html', {'contenido':contenido,
                'para_minorista':para_minorista,
                'para_mayorista':para_mayorista})

def contacto(request):
    return render(request, 'vistaprevia/contacto.html')
