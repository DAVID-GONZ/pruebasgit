import numpy as np
n = int(input('Ingrese el tamaño de la matriz cuadrada'))
# matriz =[]
# for i in range(n):
#     a = [0]*(n)
#     matriz.append(a)
# print(matriz)
#
import random

# for i in range(0,n):
#     for j in range(0,n):
#         matriz[i][j] = random.randint(1,9)
#         print(matriz[i][j], end ='\t')
#     print()
# matriz = np.array(matriz)

# def tamagno_matriz(matriz):
#     a = matriz.shape
#     n = a[0]
#     return n 

# t = tamagno_matriz(matriz)
# print(t)
# #aux =np.array([])
# aux = []
# for i in range(0,t):
#     for j in range(0,t):
#             if ((i + j) <= (t - 1)):
#                 if ((matriz[i][j]) % 2 !=0):
#                     a = matriz[i][j]
#                     print(i,j)
# print(a)
# prueba =np.array([])
# print(prueba)


def tamagno_matriz(matriz):
    t = matriz.shape[0]
    return t 

def datos_impares(matriz,t):
    aux = np.array([])
    for i in range(len(matriz)):
        for j in range(t):
                if ((i + j) <= (t - 1)) and (i + j) % 2 != 0:
                    if ((matriz[i][j]) % 2 !=0):
                        a = matriz[i][j]
                        aux = np.append(aux,a)
    return aux

def valor_menor(matriz):
    vmenor = int(np.amin(matriz))
    return vmenor

def posicion_dato_menor(matriz,t,datomenor):
    aux = []
    for i in range(len(matriz)):
        for j in range(t):
                if ((i + j) <= (t - 1)):
                    if (i + j) % 2 != 0:
                        if ((matriz[i][j]) == datomenor):
                            a = (i,j)
                            aux.append(a)
    return aux


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
    print('Las posiciones del dato menor son: ', posiciones)

def solucion(nuevamatriz):
    tamagno = tamagno_matriz(nuevamatriz)
    datosimpares = datos_impares(nuevamatriz, tamagno)
    valor_minimo = valor_menor(datosimpares)
    posiciones_valor_minimo = posicion_dato_menor(nuevamatriz, tamagno, valor_minimo)

    return valor_minimo, posiciones_valor_minimo
solucion = solucion(nuevamatriz)
