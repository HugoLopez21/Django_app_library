from django.shortcuts import render
from django.conf import settings
import json
import os 
from django.http import HttpResponse, JsonResponse
import re
from . import view_ver_socios as visualziar

#Establecer en una variable la ruta del json
ruta_json = os.path.join(settings.BASE_DIR, 'app6_practica_biblio\data\socios.json')

def dados_de_alta():
        #Lee los datos del jaosn y los devuelve.
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)  # convierte a lista/dict de Python
            return datos

def validez_dni(dni):
    #Funcion que valida el formato del dni
    patron = r'^\d{8}[A-Z]$'
    if re.match(patron, dni):
        return True
    return False




def existe_dni(dni):
    #Comprueba si el dni existe
    if validez_dni(dni): #Comprueba que dni sea valido
        datos = dados_de_alta()
        for socio in datos['socios']:
            #Recorre la lista de socios
            if socio['dni'] == dni: #Hay algun dni igual?
                return True #Existe
    return False






def recibir_formulario_alta(request):
    '''
    Recibe el formulario
    Establece los datos del nuevo socio en un diccionario
    Escribe los datos en el json con la función dar_de_alta
    '''
    socio = {
        "nombre": request.POST.get('nombre'),
        "apellidos": request.POST.get('apellidos'),
        "fecha_nacimiento": request.POST.get('fecha-nac'),
        "dni": request.POST.get('dni'),
        "foto": "/static/app6_practica_biblio/img/443021.png"
    }

    if not existe_dni(socio['dni']):
        respuesta = dar_de_alta(socio)  # Guarda en JSON y recoge el carnet generado
        
        if isinstance(respuesta, HttpResponse): #Devuleve el contenido del carnet si es un http response
            return respuesta
        # Devolvemos la respuesta en un Http response
        if isinstance(respuesta, str):
            return HttpResponse(respuesta)
        return HttpResponse(status=204)
    else:
        return HttpResponse('<h2>El dni ya existe</h2>')



def dar_de_alta(nuevo_socio):
    # Se encarga de escribir los datos en el json y llamar a una funcion externaç
    # para mostrar el carnet
    datos = dados_de_alta()

    # Agregar el nuevo socio
    datos.setdefault('socios', []).append(nuevo_socio)
    escribeJson(datos)
    
    # Devolver el HTML del socio creado para meterlo en el div y que se muestre
    return visualziar.muestra_socio_selec(nuevo_socio['dni'], 'Socio dado de alta con éxito')

def escribeJson(datos):
    # Escribimos en el archivo JSON
    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent="\t")
        