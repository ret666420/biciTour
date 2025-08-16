from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from recorridos import views as recorridos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recorridos_views.principal, name='principal'),
    path('detalle_recorrido/', views.detalle_recorrido, name='detalle_recorrido'),
    path('preinscripcion/', recorridos_views.preinscripcion, name='preinscripcion'),  # <-- Cambia el name aquí
    path('exitoso/', recorridos_views.exitoso, name='exitoso'),  # <-- Cambia el name aquí
    path('nosotros/', recorridos_views.nosotros, name='nosotros'),  # <-- Cambia el name aquí


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

