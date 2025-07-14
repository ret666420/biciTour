from django.db import models





class Recorridos(models.Model):
    estado = models.CharField(max_length=100, verbose_name="Estado del Recorrido")

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado del Recorrido"
        verbose_name_plural = "Estados de los Recorridos"

