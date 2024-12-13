from django.urls import path, include
from .views import *
#API
from rest_framework import routers

router = routers.DefaultRouter()
router.register('persona', PersonaViewSet)
router.register('episodio', EpisodioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('lista/', listarEmpleadosAPI, name="listarEmpleadosAPI"),
    path('', index, name="index"),
    path('add', add, name="add"),
    path('update/<id>', update, name="update"),
    path('delete/<id>', delete, name="delete"),
    path('add_episodios/', add_episodios, name="add_episodios"),
    path('update_episodios/<id>', update_episodios, name="update_episodios"),
    path('delete_episodios/<id>', delete_episodios, name="delete_episodios"),
    ]


