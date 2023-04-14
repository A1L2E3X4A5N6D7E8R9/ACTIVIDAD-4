#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contadorascendente(num):
    cont=0
    while cont<=num:
        print(cont)
        cont+=1
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.

def contadordescendete(num):
    cont=num
    while cont>=1:
        print(cont)
        cont-=1
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def sumanumeros(num):
    suma=0
    cont= 0
    while suma<=num:
        suma+=1
        cont+=suma
    return cont

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

def factorial (num):
    cont=1
    multi=1
    while cont<=num:
        multi= multi*cont
        cont+=1
    return multi

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random 
def aleatorio(num):
    adivinar=0
    while adivinar != num:
        adivinar= int(input("adivine al numero:"))
        if adivinar <= num:
            print("el numero que buscas es menor")
        elif adivinar<=num:
            print("el numero que buscas es mayor ")
        else:
            print("¡bien hecho!, haz adivinado el numero")

num= random.randint(1,101)
aleatorio(num)


#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contar_vocales(cadena):
    cont=0
    vocales=["a","e","i","o","u"]
    indice=0
    while indice< len(cadena):
         if cadena[indice] in vocales:
              cont+=1
              indice+=1
              return cadena
#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def numeros_pares(num):
    suma = 0
    i = 0

    while i <= num:
        if i % 2 == 0:
            suma += i
        i += 1
    return print("La suma de todos los números pares desde 0 hasta", num, "es:", suma)
     
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.

def potencia(num,exponente):
     resultado=1
     cont=1
     while cont <=exponente:
          resultado= resultado*num
          cont+=1
          print(resultado)

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio(lista_num):
     suma=0
     contar=0
     while contar<(len(lista_num)):
          suma=suma+lista_num[contar]
          contar+=1
          print("el promedio es:",suma/len(lista_num))

#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco
def contador_palabras(cadena_text):
     contador=0
     indice=0
     while indice<len(cadena_text):
          if cadena_text[indice]:
               contador+=1
               indice+=1
               print(contador)