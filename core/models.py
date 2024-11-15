from django.db import models # type: ignore

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=50)
    verificado = models.BooleanField()
    avatar = models.ImageField (null=True, blank=True)
    linkendin = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=50)
      
    def __str__(self):
        return self.nombre
    
class Episodio(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    anfitrion = models.ForeignKey(Persona, on_delete=models.CASCADE)
    suscriptores = models.IntegerField()
    likes = models.IntegerField()
    comentarios = models.IntegerField()
      
    def __str__(self):
        return self.titulo
      
      