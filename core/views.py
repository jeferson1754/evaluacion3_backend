from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import *
from .forms import *
from rest_framework import viewsets, filters
from .serializers import *

from rest_framework.renderers import JSONRenderer
# Create your views he
from django_filters.rest_framework import DjangoFilterBackend
import requests
#VIESEt

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ocupacion','verificado']
    search_fields = ['nombre','whatsapp']
    renderer_classes=[JSONRenderer]

    
class EpisodioViewSet(viewsets.ModelViewSet):
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer
    renderer_classes=[JSONRenderer]
    
    
def listarEmpleadosAPI(request):
    response = requests.get("http://127.0.0.1:8000/api/persona/")
    repo = requests.get("http://127.0.0.1:8000/api/episodio/")
    
    if response.status_code == 200:
        persona = response.json()  
    else:
        persona = []
        
    if repo.status_code == 200:
        episodio = repo.json()  
    else:
        episodio = []
        
    datos = {
        'listapersonas': persona,
        'listaepisodios': episodio
    }
        
    return render(request, 'core/persona/listar.html',datos)


def index(request):
    # ACCEDER A LA BD
    listpersonas = Persona.objects.all()  # SELECT * FROM Persona
    list_episodios = Episodio.objects.select_related(
        'anfitrion').all()  # SELECT * FROM Episodio

    # MEDIO DE TRANSPORTE
    datos = {
        'listapersonas': listpersonas,
        'listaepisodios': list_episodios
    }

    return render(request, 'core/index.html', datos)


def add(request):

   # MEDIO DE TRANSPORTE
    datos = {
        'form': PersonaForm()
    }

    if request.method == 'POST':
        formulario = PersonaForm(request.POST, files=request.FILES)
        if formulario .is_valid():
            formulario.save()
            datos['msj'] = "Persona creada correctamente!"

    return render(request, 'core/persona/add.html', datos)


def update(request, id):
    # MEDIO DE TRANSPORTE
    personas = Persona.objects.get(id=id)
    datos = {
        'form': PersonaForm(instance=personas)
    }

    if request.method == 'POST':
        formulario = PersonaForm(
            data=request.POST, instance=personas, files=request.FILES)
        if formulario .is_valid():
            formulario.save()
            datos['msj'] = "persona actualizada correctamente!"
            datos['form'] = formulario

    return render(request, 'core/persona/update.html', datos)


def delete(request, id):
    # Obtener la persona usando get_object_or_404 para manejar excepciones si no existe
    persona = get_object_or_404(Persona, id=id)
    persona.delete()  # Eliminar el objeto de la base de datos

    # Redirigir a la vista 'index' después de la eliminación
    return redirect('index')


def add_episodios(request):

   # MEDIO DE TRANSPORTE
    datos = {
        'form': EpisodioForm()
    }

    if request.method == 'POST':
        formulario = EpisodioForm(request.POST, files=request.FILES)
        if formulario .is_valid():
            formulario.save()
            datos['msj'] = "Episodio creado correctamente!"

    return render(request, 'core/episodios/add.html', datos)


def delete_episodios(request, id):
  # Obtener la persona usando get_object_or_404 para manejar excepciones si no existe
    episodio = get_object_or_404(Episodio, id=id)
    episodio.delete()  # Eliminar el objeto de la base de datos

    # Redirigir a la vista 'index' después de la eliminación
    return redirect('index')


def update_episodios(request, id):

  # MEDIO DE TRANSPORTE
    episodios = Episodio.objects.get(id=id)
    datos = {
        'form': EpisodioForm(instance=episodios)
    }

    if request.method == 'POST':
        formulario = EpisodioForm(
            data=request.POST, instance=episodios, files=request.FILES)
        if formulario .is_valid():
            formulario.save()
            datos['msj'] = "episodio actualizado correctamente!"
            datos['form'] = formulario

    return render(request, 'core/episodios/update.html', datos)
