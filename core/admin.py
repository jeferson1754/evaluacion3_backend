from django.contrib import admin
from django.db.models import Count
from .models import Episodio, Persona

# Función reutilizable para contar episodios
def episodios_count_method(obj):
    return obj.episodio_set.count()

episodios_count_method.short_description = 'Cantidad de Episodios'

# Personalización del administrador para la tabla Persona
class PersonaAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ['nombre', 'ocupacion', 'verificado', 'avatar', 'linkendin', 'whatsapp', episodios_count_method]
    
    # Campos para buscar en la tabla
    search_fields = ['nombre', 'ocupacion', 'episodio__nombre']  # Permite buscar por nombre de episodio relacionado
    
    # Número de elementos a mostrar por página (paginación)
    list_per_page = 5
    
    # Filtros en el panel de administración para facilitar la búsqueda
    list_filter = ['ocupacion', 'verificado']
    
    # Configuración de ordenación por defecto
    ordering = ['nombre']
    
    # Campos en los que se puede hacer clic para ver detalles
    list_display_links = ['nombre']

    # Mostrar un texto en el panel para ayudar a visualizar si está verificado o no
    def verificado_status(self, obj):
        return "Sí" if obj.verificado else "No"
    verificado_status.short_description = 'Verificado'
    
    # Mostrar imagen de avatar en el panel de administración (si la imagen es pequeña)
    def avatar_thumbnail(self, obj):
        if obj.avatar:
            return f'<img src="{obj.avatar.url}" width="50" height="50" />'
        return '-'
    avatar_thumbnail.short_description = 'Avatar'
    avatar_thumbnail.allow_tags = True

    # Anotar la cantidad de episodios en la consulta para mejor rendimiento
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        
        # Buscar por cantidad de episodios (solo si se introduce un número)
        if search_term.isdigit():
            queryset = queryset.annotate(episodios_count=Count('episodio'))
            queryset = queryset.filter(episodios_count=int(search_term))
        
        return queryset, use_distinct


# Personalización del administrador para la tabla Episodio


# Registrar modelos en el panel de administración de Django
admin.site.register(Episodio)
admin.site.register(Persona, PersonaAdmin)
