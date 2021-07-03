#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""


mensaje = str(input('INTRODUZCA LA LETRA A TRADUCIR'))
#codigo_morse = mensaje.strip().split(' ')
#print(codigo_morse)
def lista_letras(codigo):
    global mensaje_traducido
    diccionario = {'.-':'A','-...':'B','-.-.':'C',
            '-..':'D', '.':'E','..-.':'F','--.':'G',
            '....':'H','..':'I','.---':'J','-.-':'K',
            '.-..':'L','--':'M','-.':'N','---':'O',
            '.--.':'P','--.-':'Q','.-.':'R','...':'S',
            '-':'T', '..-':'U','...-':'V','.--':'W',
            '-..-':'X','-.--':'Y','--..':'Z','/':' ',' ':''}

    codigo_morse = codigo.strip().split(' ')

    mensajeg = []
    for i in codigo_morse:
        letra = diccionario.get(i)
        mensajeg.append(letra)
        mensaje_traducido = ''.join(map(str,mensajeg))
    return mensaje_traducido

lista_letras = lista_letras(mensaje)
print(lista_letras)
print(type(lista_letras))

#print(diccionario)
#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 

#print(type(diccionario))

"""Fin espacio para programar funciones propias"""

# def traductor_a_espanol(mensaje_a_traducir):
#     #PROGRAMA ACÁ TU SOLUCIÓN
    
    
#     return mensaje_traducido

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_a_espanol)