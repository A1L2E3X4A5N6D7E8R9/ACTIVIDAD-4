###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
from ejercicioswhile import*
opcion=1
while opcion>=0 and opcion<=10:
    print("#########MENU DE OPCIONES#########")
    print("1. CONTADOR ASCENDETE")
    print("2. CONTADOR DESCENDETE")
    print("3. SUMA DE NUMEROS")
    print("4. FACTORIAL")
    print("5. ADIVINAR EL NUMERO")
    print("6. CONTADOR DE VOCALES")
    print("7. SUMA DE NUMEROS PARES")
    print("8. CALCULO POTENCIAL")
    print("9. CALCULO PROMEDIO")
    print("10. CONTADOR DE PALABRAS")
    print("0. SALIR")
    
    opcion=int(input("ingrese una opcion:"))
    if opcion==0:
        print("acaba de seleccionar salir:")
    elif opcion ==1:
        print("acaba de seleccionar contador ascedente:")
        num= int(input("ingrese el numero:"))
        contadorascendente(num)

    elif opcion ==2:
        print("acaba de seleccionar contador descendete:")
        num=int(input("ingrese el valor"))
        contadordescendete(num)

    elif opcion==3:
        print("acaba de seleccionar suma de numeros:")
        num=int(input("ingrese el numero:"))
        print(sumanumeros(num))

    elif opcion==4:
        print("acaba de selccionar factorial")
        num=int(input("ingrese el numero:"))
        factorial(num)

    elif opcion ==5:
        print("acaba de seleccionar adivina el numero")
    
    elif opcion ==6:
        print("acaba de seleccionar contador de vocales")
        vocales=input("ingrese la cadena de vocales")
        print(contar_vocales(vocales))
                  
    elif opcion==7:
        print("acaba de seleccionar suma de numeros pares")
        num=int(input("ingrese el valor"))
        numeros_pares(num)

    elif opcion==8:
        print("acaba de seleccionar calculo de potencia")
        num=int(input("ingrese el valor "))
        exponente=int(input("ingrese el exponente"))
        potencia(num,exponente)
    elif opcion==9:
        ("acaba de seleccionar calculo promedio")
        lista_num = input("Ingresa una lista de números separados por comas: ")
        lista_num = lista_num.split(",")
        promedio(lista_num)
    elif opcion==10:
        print("acaba de seleccionar contador de palabras")
        cadena_text=input("ingrese la cadena de texto:")
        contador_palabras(cadena_text)