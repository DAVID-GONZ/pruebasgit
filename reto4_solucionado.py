#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
# /from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


def process_data(operations, default_page):
    pila_atras = []
    pila_adelante = []
    pagina_actual = default_page
    for i in operations:
        if i == "atras":
            last_back = pila_atras.pop()
            pila_adelante.append(pagina_actual)
            pagina_actual = last_back
        elif i == "adelante":
            last_forward = pila_adelante.pop()
            pila_atras.append(pagina_actual)
            pagina_actual = last_forward
        elif i is not None and i != str(pagina_actual):
            pila_atras.append(pagina_actual)
            pagina_actual = str(i)
            pila_adelante = []
    return pila_atras, pagina_actual, pila_adelante

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

operaciones_usuario = ["udea.edu.co", "ingeniaudea.co", "twitter.com", "atras",
                       "atras", "adelante", "facebook.com", "facebook.com"]
pagina_default = "google.com"
operaciones_usuario2 = ['udemy.com', 'atras', 'adelante', 'facebook.com',
                       'atras', 'atras', 'adelante', 'udemy.com', 'adelante']
pagina_default2 = 'google.com'

processing = process_data(operaciones_usuario, pagina_default)
print(processing)


"""Fin espacio para programar funciones propias"""

# def actualizar_estado_pestana(operaciones_usuario, pagina_default):
#     #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
#
#
#
#     return pila_atras, pagina_actual, pila_adelante
#
# """
# NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
# Esta línea de código que sigue, permite probar si su ejercicio es correcto
# Por favor NO ELIMINARLA
# """
# pruebas_codigo_estudiante(actualizar_estado_pestana)