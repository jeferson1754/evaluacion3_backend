from django import forms # type: ignore
from django.forms import ModelForm # type: ignore
from .models import *

class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = ['nombre','ocupacion','verificado','avatar','linkendin', 'whatsapp']
    
        
class EpisodioForm (ModelForm):
    
    numero = forms.IntegerField (min_value=1)
    suscriptores = forms.IntegerField (min_value=1)    
    likes = forms.IntegerField (min_value=1)
    comentarios = forms.IntegerField (min_value=1)        
    
    class Meta:
        model = Episodio
        fields = ['titulo','duracion','numero','descripcion','anfitrion','suscriptores','likes','comentarios']
        