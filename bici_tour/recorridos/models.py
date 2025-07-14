from django.db import models





class Recorridos(models.Model):
    estado = models.CharField(max_length=100, verbose_name="Estado del Recorrido")

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado del Recorrido"
        verbose_name_plural = "Estados de los Recorridos"


class Recorrido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    kilometros = models.DecimalField(max_digits=5, decimal_places=2)  # ejemplo: 120.50 km
    tiempo_estimado = models.DurationField()  # duración en horas:minutos
    punto_inicio = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2)  # ejemplo: 1500.00
    descripcion = models.TextField()
    fotografia = models.ImageField(
        null=True,
        upload_to='fotos/',
        verbose_name="Fotografia"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ciudad} - {self.fecha} - {self.hora}"

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ['-fecha', '-hora']
