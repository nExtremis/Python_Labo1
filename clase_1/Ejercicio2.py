def informarEdad(edad,nombre):
    if edad >= 18:
        print(f"{nombre} es mayor de edad")
    elif edad < 18 and edad >=13:
        print(f"{nombre} es adolecente")
    else:
        print(f"{nombre} es niño/a")      

nombre =  input("Por favor ingrese su nombre: ")
while not nombre.isalpha():
    nombre =  input("Error. Por favor vuelva a ingresar su nombre: ")


edad = input("Por favor ingrese su edad: ")
flagInt = 0
if edad.isdigit():
    edad = int(edad)
    flagInt = 1
while flagInt != 1:
    edad = input("Error. Por favor vuelva a ingresar su edad: ")
    if edad.isdigit():
        edad = int(edad)
        flagInt = 1 

informarEdad(edad,nombre)