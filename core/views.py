from django.shortcuts import render, redirect, get_object_or_404# type: ignore
from .models import * 
from .forms import *

# Create your views here.
def index(request):
    # ACCEDER A LA BD
    listpersonas = Persona.objects.all()  # SELECT * FROM Persona
    list_episodios = Episodio.objects.select_related('anfitrion').all()# SELECT * FROM Episodio

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
        
    return render (request, 'core/persona/add.html', datos)

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
        
    return render (request, 'core/episodio/add.html')

def delete_episodios(request):
        
    return render (request, 'core/episodio/delete.html')

def list_episodios(request):
    
  # ACCEDER A LA BD
    listpersonas = Episodio.objects.all()  # SELECT * FROM Empleado

    # MEDIO DE TRANSPORTE
    datos = {
        'lista': listpersonas
    }

    return render(request, 'core/episodios/list.html', datos) 
        
def update_episodios(request):
        
    return render (request, 'core/episodio/update.html')