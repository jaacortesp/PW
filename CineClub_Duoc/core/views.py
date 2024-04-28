from django.shortcuts import render, redirect
from django.conf.urls.static import static
import json
import urllib.request

def read_json_from_url(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data

json_data = read_json_file('https://github.com/jaacortesp/json_api/blob/main/api1.json')

# Create your views here.

def index(request):
     return render(request, 'core/index.html')

def posts(request):
     return render (request, 'core/posts.html')

def datos_ingresados(request):
     return render(request, 'core/datos_ingresados.html')

def detalle(request):
     return render(request, 'core/detalle.html')

def formulario(request):
     return render(request, 'core/formulario.html')

def iniciar_sesion(request):
     return render(request, 'core/iniciar-sesion.html')

