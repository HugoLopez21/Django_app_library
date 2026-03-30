from django.urls import path
from .views import view_sesion, view_ver_socios, view_form

app_name = 'app6_practica_biblio'
urlpatterns = [
    path("", view_sesion.base, name="base"),
    
    # VISTAS DE SESION
    path('refrescar_sesion/', view_sesion.refrescar_sesion, name='refrescar_sesion'),
    path('verificar_sesion/', view_sesion.verificar_sesion, name='verificar_sesion'),
    path('iniciar_sesion/', view_sesion.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', view_sesion.cerrar_sesion, name='cerrar_sesion'),
    
    #VISTAS DE MOSTRAR SOCIOS
    path('mostrar_socio_seleccionado/', view_ver_socios.recoge_socio_selec, name='mostrar_socio_seleccionado'),
    path('mostrar_socios/', view_ver_socios.muestra_socios, name='mostrar_socios'),

    #VISTAS DE ALTA DE USUARIOS CON FORMULARIO
    path('recibir_formulario_alta/', view_form.recibir_formulario_alta, name='recibir_formulario_alta'),


]