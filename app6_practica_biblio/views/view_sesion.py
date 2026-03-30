from django.shortcuts import render
from django.http import JsonResponse, HttpResponse




def base(request):
    return render(request, 'app6_practica_biblio/base.html')


def refrescar_sesion(request):
    # Reinicia el tiempo de la variable de sesión cundo se llame
    try:
        request.session.set_expiry(600)
        print('Tiempo de sesion reinciado')
        return HttpResponse('ok')

    except Exception as e:
        return JsonResponse({
            'status': 'error', 
            'mensaje': f'Error interno: {str(e)}'
        })


def verificar_sesion(request):
    #Comprueba si la sesion sigue activa o no
    activa = request.session.get('sesion_activa', False)
    
    print(f'sesion: {activa}')
    return JsonResponse({'estado_sesion': activa})

def iniciar_sesion(request):
    # Crea la variable de sesion con un tiempo de 10 mins
    try:
        request.session.flush() # Limpia la sesion anterior
        request.session.set_expiry(600)  #10 minutos
        request.session['sesion_activa'] = True
        
        print('Sesíon activada')
        return JsonResponse({
            'status': 'ok', 
            'mensaje': 'Sesión de 10 minutos iniciada.'
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error', 
            'mensaje': f'Error interno: {str(e)}'
        })
    
def cerrar_sesion(request):
    #Borra la sesion y envia mensaje de estado
    try:
        request.session.flush()
        print(f'Sesión borrada')
        return JsonResponse({
            'status': 'ok', 
            'mensaje': 'Sesión cerrada'
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error', 
            'mensaje': f'Error interno: {str(e)}'
        })

    
    
