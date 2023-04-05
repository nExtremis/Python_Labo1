flagInt = 0
edad = input("Ingrese su edad: ")
if edad.isdigit() and int(edad) > 0 and int(edad) < 100:
    edad = int(edad)
    flagInt = 1
while flagInt != 1:
    edad = input("Error. Por favor ingrese su edad: ")
    if edad.isdigit():
        edad = int(edad)
        flagInt = 1

estadoCivil = input("Por favor ingrese su estado civil: ").lower()
while not estadoCivil.isalpha() and not(estadoCivil == "soltero" or estadoCivil=="casado"):
    estadoCivil = input("Por favor ingrese su estado civil: ").lower()


if edad < 18 and estadoCivil != "soltero":
    print("Es muy pequeño para NO ser soltero.")