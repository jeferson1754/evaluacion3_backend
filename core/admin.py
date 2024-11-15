from django.contrib import admin
from .models import *

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre','ocupacion','verificado']
    search_fields = ['nombre','ocupacion']
    list_per_page = 2
    
    
admin.site.register(Episodio)
admin.site.register(Persona,PersonaAdmin)