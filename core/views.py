from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import *
from .forms import *

# Create your views here.


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
