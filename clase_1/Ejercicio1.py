def incremento_10porcent(sueldo,nombre):
    sueldo = (sueldo * 100)/10 + sueldo
    print(f"El sueldo de {nombre} con un incremento de un 10% es : ${sueldo} ")

nombre =  input("Por favor ingrese su nombre: ")
while not nombre.isalpha() :
    nombre =  input("Error. Por favor ingrese su nombre correctamente: ")
    nombre = str(nombre)



sueldo = input("Por favor ingrese su sueldo: ")
flagInt = 0
if sueldo.isdigit():
    sueldo = int(sueldo)
    flagInt = 1
while  flagInt != 1 :
    sueldo = input("Error. Por favor ingrese su sueldo: ")
    if sueldo.isdigit():
        sueldo = int(sueldo)
        flagInt = 1



incremento_10porcent(sueldo,nombre)

