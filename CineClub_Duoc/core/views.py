from django.shortcuts import render, redirect
from django.conf.urls.static import static

# Create your views here.

def home(request):
     return render(request, 'core/home.html')

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

