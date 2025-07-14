from django.contrib import admin
from .models import Recorrido, Preinscripcion

class RecorridoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('fecha', 'hora', 'estado', 'ciudad', 'kilometros', 'tiempo_estimado', 'punto_inicio', 'costo')
    search_fields = ('estado', 'ciudad', 'punto_inicio')
    date_hierarchy = 'created'
    list_filter = ('estado', 'ciudad', 'fecha')

admin.site.register(Recorrido, RecorridoAdmin)


class adminPreinscripcion(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'ciudad', 'estado', 'recorrido', 'created')
    search_fields = ('nombre', 'correo', 'telefono', 'ciudad', 'estado')
    list_filter = ('recorrido', 'estado')
    ordering = ('-created',)
    date_hierarchy = 'created'

admin.site.register(Preinscripcion, adminPreinscripcion)
