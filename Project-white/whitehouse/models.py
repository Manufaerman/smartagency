from django.core.exceptions import AppRegistryNotReady
from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)

class Categorias(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre

class Vivienda(models.Model):
    nombre = models.CharField(max_length=30)
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity= models.IntegerField()
    foto1 = models.ImageField(upload_to = 'whitehouse')
    foto2 = models.ImageField(upload_to = "whitehouse")
    foto3 = models.ImageField(upload_to = "whitehouse")
    country =models.CharField(max_length=300)
    city =models.CharField(max_length=300)
    neiborhood =models.CharField(max_length=300)
    categoria = models.ManyToManyField(Categorias)
    direccion = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} with {self.beds} beds for {self.capacity}'

    class Meta:
        verbose_name='Vivienda'
        verbose_name_plural='Viviendas'



class reservas(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    numero = models.IntegerField(blank=True)
    fecha_entrada = models.DateField() 
    fecha_salida = models.DateField()
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Vivienda availability',
    )
    
    @property
    def is_booked(self):
        if self.fecha_salida and date.today() > self.fecha_salida:
            return True
        return False

    class Meta:
        verbose_name='Reserva'
        verbose_name_plural='Reservas'
        ordering = ['vivienda','fecha_salida']

    def __str__(self) -> str:
        return f'{self.user} has booked {self.vivienda}  room, from {self.fecha_entrada} to {self.fecha_salida}'