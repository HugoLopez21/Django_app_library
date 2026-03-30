from django.shortcuts import render
import os
import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings

ruta_json = os.path.join(settings.BASE_DIR, 'app6_practica_biblio\data\socios.json')

#Recibe el socio por metodo get y ejecuta la funcion enviandole el dni y un mensane
def recoge_socio_selec(request):
    if request.method == 'GET':
        if (request.GET.get("socio")):
            dni_socio = request.GET.get("socio");
            return HttpResponse(muestra_socio_selec(dni_socio, 'Mostrando socio...'))
        else:
            return HttpResponse('<h2>Selecciona a un socio primero</h2>')
      
#Recibe un dni y un mensaje y lo envia al cliente con formato html     
def muestra_socio_selec(dni_socio, mensaje):
    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            datos = json.load(file)
    except Exception as e:
        datos = {"error": str(e)}


    for unico_socio in datos['socios']:
        if unico_socio['dni'] == dni_socio:
            return f'''
                <h2>{mensaje}</h2>
                <div class="carnet">
                    <div class="carnet-izq">
                        <img id="foto" src="{unico_socio['foto']}">
                        <p id="dni"> DNI: {unico_socio['dni']}</p>
                    </div>
                    <div class="carnet-der">
                        <h3>Biblioteca municipal</h3>
                        <p id="nombre_completo">{unico_socio['apellidos']} , {unico_socio['nombre']}</p>
                        <p id="f_nac"> Fecha de nacimiento: {unico_socio['fecha_nacimiento']}</p>
                    </div>
                </div>
            '''


#Envia los socios al cliente para mostrarlo segun el orden
def muestra_socios(request):
    '''
    1. Recoge del formulario el orden
    2. Recoge los datos del json (socios.jason) y guarda la lista de socios
    3. Comprueba que orden mostar
    4. Recorre los socios por el nombre y los ordena
    5. Devuelve el html donde se muestran los socios pasandole los datos
    '''
    if request.method == 'GET':
        orden_mostrar = request.GET.get('orden')

    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            datos = json.load(file)
            socios = datos.get("socios", [])
    except Exception as e:
        datos = {"error": str(e)}


    if orden_mostrar == 'asc':
        socios_ordenados = sorted(socios, key=lambda socio: socio["nombre"])
    
    elif orden_mostrar == 'desc':
        socios_ordenados = sorted(socios, key=lambda socio: socio["nombre"], reverse=True)

    else:
        socios_ordenados = socios

    #Nueva variable
    contenido_html = ''
    
    for unico_socio in socios_ordenados:
        #En vez de reemplazar el contenido de la  variable lo va sumando para mostrar todos
        contenido_html += f'''
                <div class="carnet">
                    <div class="carnet-izq">
                        <img id="foto" src="{unico_socio['foto']}">
                        <p id="dni"> DNI: {unico_socio['dni']}</p>
                    </div>
                    <div class="carnet-der">
                        <h3>Biblioteca municipal</h3>
                        <p id="nombre_completo">{unico_socio['apellidos']} , {unico_socio['nombre']}</p>
                        <p id="f_nac"> Fecha de nacimiento: {unico_socio['fecha_nacimiento']}</p>
                    </div>
                </div>
            '''
    return HttpResponse(contenido_html) 
             


