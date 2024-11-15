from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('add', add, name="add"),
    path('list', list, name="list"),   
    path('update/<id>', update, name="update"),
    path('delete/<id>', delete, name="delete"),
    path('add_episodios/', add_episodios, name="add_episodios"),
    path('list_episodios/', list_episodios, name="list_episodios"),
    path('update_episodios/<id>', update_episodios, name="update_episodios"),
    path('eliminar/<id>', delete, name="eliminar"),
    ]


