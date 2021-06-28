import numpy as np

#Tamaño de la matríz
def tamagno_matriz(matriz):
    a = matriz.shape[0]
    return a


def datos_impares(matriz, tamagno):
    aux = np.array([])
    for i in range(tamagno):
        for j in range(tamagno):
            if (i + j) <= (tamagno - 1):
                if (matriz[i][j]) % 2 != 0:
                    a = matriz[i][j]
                    aux = np.append(aux, a)
    return aux


def valor_menor(matriz):
    vmenor = int(np.amin(matriz))
    return vmenor


def posicion_dato_menor(matriz, tamagno, datomenor):
    aux = []
    for i in range(tamagno):
        for j in range(tamagno):
            if (i + j) <= (tamagno - 1) and (matriz[i][j]) % 2 != 0:
                if matriz[i][j] == datomenor:
                    a = (i, j)
                    aux.append(a)
    return aux

nuevamatriz = np.random.randint(0,10,(n*n)).reshape(n,n)
def solucion(A):
    tamagno = tamagno_matriz(A)
    datosimpares = datos_impares(A, tamagno)
    valor_minimo = valor_menor(datosimpares)
    posiciones_valor_minimo = posicion_dato_menor(A, tamagno, valor_minimo)

    return valor_minimo, posiciones_valor_minimo


"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
#NO MODIFICAR"""
matriz_entrada = np.array([[89, 13, 23, 72],
       [29, 11, 81, 62],
       [27, 26, 88, 33],
       [ 5, 78, 11, 11]])
menor_estudiante = solucion(matriz_entrada)[0]
posiciones_menor_estudiante = solucion(matriz_entrada)[1]
print("MATRIZ ENTREGADA:\n", matriz_entrada,"\n")
print("===SALIDA ESPERADA===\nMenor = ", 5,"\nPosiciones donde está el menor = ", [(3, 0)],"\n")
print("===TU SALIDA===:\nMenor = ", menor_estudiante,"\nPosiciones donde está el menor = ", posiciones_menor_estudiante,"\n")
if menor_estudiante == 5 and  set(posiciones_menor_estudiante) == set([(3, 0)]):
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")

#pruebas de validaci[on]
n = int(input('Ingrese el tamaño de la matriz cuadrada'))
nuevamatriz = np.random.randint(0,10,(n*n)).reshape(n,n)
print(nuevamatriz)
print('la longitud de la matriz es: ',len(nuevamatriz))
tamagno = tamagno_matriz(nuevamatriz)
print('ESTE ES EL TAMAÑO de la matriz:', tamagno)
datosimpares = datos_impares(nuevamatriz,tamagno)
print('Array con datos impares: ', datosimpares)
valormenor = valor_menor(datosimpares)
print('El valor menor es :', valormenor)
posiciones = posicion_dato_menor(nuevamatriz,tamagno,valormenor)
print('Las posiciones del dato menor son: ', posiciones)c