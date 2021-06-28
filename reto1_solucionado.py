from clase_vectores import Vector
import random
import math
def solucion():
    a = random.randint(15,30)
    v = Vector(a)
    for i in range(1,a+1):
        v.vector[i] = random.randint(1,9999)         
        v.vector[0] += 1
    suma = 0
    for i in range(1,a+1): 
        if es_primo(v.vector[i]) or comienza_digito_impar(v.vector[i]): #
            suma += v.vector[i]
    return v, suma

def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False  
    return True

def comienza_digito_impar(n):
    d = str(n)[0] #Completar
    d = int(d) #Completar
    if d % 2 ==1:
            return True
    return False

def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.vector[0] + 1):
        print(vector.vector[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()
a, suma = solucion()
imprimeVector(a, 'Original')
print("Suma: ", suma)