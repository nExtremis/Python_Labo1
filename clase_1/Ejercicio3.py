#Ejercicio 3:
#Ingresar 5 números enteros, distintos de cero.
#Informar:
#a. Cantidad de pares e impares.
#b. El menor número ingresado.
#c. De los pares el mayor número ingresado.
#d. Suma de los positivos.
#e. Producto de los negativos.

def esPar(numero):
    if numero%2 == 0:
        return True
    else:
        return False

cantNumPares = 0
cantNumImpares = 0
esElMenor = 0
esElMayorPar = 0
flagPar = 0
sumaDePositivos = 0
productoDeNegativos = 1



for i in range(1,6):
    flagInt = 0
    numero = input("Por favor ingrese un numero: ")
    if numero.lstrip("-").isdigit():
        numero = int(numero)
        flagInt = 1
    while flagInt != 1:
        numero = input("Error. Por favor ingrese un numero: ")
        if numero.lstrip("-").isdigit():
            numero = int(numero)
            flagInt = 1

    if esPar(numero):
        cantNumPares = cantNumPares + 1
        if flagPar == 0:
            esElMayorPar = numero
            flagPar = 1
        elif numero > esElMayorPar :
            esElMayorPar = numero    
    else:
        cantNumImpares = cantNumImpares + 1  

    if i == 1:
        esElMenor = numero
    elif numero < esElMenor :
        esElMenor = numero   

    if numero > 0 :
        sumaDePositivos = sumaDePositivos + numero 
    elif numero < 0:
        productoDeNegativos = productoDeNegativos * numero    

print(f"La cantidad de números pares ingresados es : {cantNumPares} y la cantidad de números impares ingresados es : {cantNumImpares}")
print(f"El menor número ingresado es : {esElMenor}")
print(f"El mayor número par ingresado es : {esElMayorPar}")
print(f"La suma de los números positivos ingresados es : {sumaDePositivos}")
print(f"El producto de los numeros negativos ingresados es : {productoDeNegativos}")
