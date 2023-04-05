estadiaBase = 15000
aumento = 0
precioFinal = 0
estacionIngresada = input("Por favor ingrese una estación del año(Invierno/Verano/Otoño/Primavera : ").lower()
while not estacionIngresada != "invierno" and  not estacionIngresada != "verano" and not estacionIngresada != "otoño" and not estacionIngresada != "primavera":
    estacionIngresada = input("Error.Por favor ingrese una estación del año(Invierno/Verano/Otoño/Primavera : ").lower()
localidadIngresada = input ("Por favor ingrese localidad(Bariloche/Cataratas/Mar del Plata/Córdoba: ")
while  not localidadIngresada != "bariloche" and  not localidadIngresada != "cataratas" and not localidadIngresada != "mar del plata" and not localidadIngresada != "córdoba":
    localidadIngresada = input ("Error.Por favor ingrese localidad(Bariloche/Cataratas/Mar del Plata/Córdoba: ")

match localidadIngresada:
    case "bariloche":
        if estacionIngresada == "invierno":
            precioFinal = estadiaBase + estadiaBase*20/100
        elif estacionIngresada == "verano":    
            precioFinal = estadiaBase - estadiaBase*20/100
        else:   
            precioFinal = estadiaBase + estadiaBase*10/100
    case "cataratas":
        if estacionIngresada == "invierno":
            precioFinal = estadiaBase - estadiaBase*10/100
        else:   
            precioFinal = estadiaBase + estadiaBase*10/100
    case "córdoba":
        if estacionIngresada == "invierno":
            precioFinal = estadiaBase - estadiaBase*10/100
        elif estacionIngresada == "verano":   
            precioFinal = estadiaBase + estadiaBase*10/100
        else:
            precioFinal = estadiaBase
    case "mar del plata":
        if estacionIngresada == "invierno":
            precioFinal = estadiaBase - estadiaBase*20/100
        elif estacionIngresada == "verano":   
            precioFinal = estadiaBase + estadiaBase*20/100
        else:
            precioFinal = estadiaBase + estadiaBase*10/100    

print(f"el precio final a pagar es : {precioFinal}")