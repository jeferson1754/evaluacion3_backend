from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('add', add, name="add"),
    path('update/<id>', update, name="update"),
    path('delete/<id>', delete, name="delete"),
    path('add_episodios/', add_episodios, name="add_episodios"),
    path('update_episodios/<id>', update_episodios, name="update_episodios"),
    path('delete_episodios/<id>', delete_episodios, name="delete_episodios"),
    ]


