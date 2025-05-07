from django.db import models

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=20, choices=[('activa', 'Activa'), ('cancelada', 'Cancelada')], default='activa')

    def __str__(self):
        return f'{self.cliente} - {self.habitacion} ({self.fecha_entrada} a {self.fecha_salida})'

class Resena(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f'{self.cliente} -> {self.habitacion} ({self.calificacion})'
