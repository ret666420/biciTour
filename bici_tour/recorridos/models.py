from django.db import models



class Recorrido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    kilometros = models.DecimalField(max_digits=5, decimal_places=2)  
    tiempo_estimado = models.DurationField() 
    punto_inicio = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2) 
    
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


class Recorridos(models.Model):
    estado = models.CharField(max_length=100, verbose_name="Estado del Recorrido")

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado del Recorrido"
        verbose_name_plural = "Estados de los Recorridos"

class Preinscripcion(models.Model):
    recorrido = models.ForeignKey(
        Recorrido,
        on_delete=models.CASCADE,
        verbose_name="Recorrido"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Preinscripción"
        verbose_name_plural = "Preinscripciones"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.nombre} - {self.recorrido}"