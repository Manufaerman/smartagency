from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class servicio(models.Model):
    nombre = models.CharField(max_length=30)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.nombre



