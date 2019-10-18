linea = input("Ingresar en orden: Nombre de estación, Temperatura, Humedad:  ")

sumaTemperaturas = 0
sumaHumedades = 0
cantidadDeElementos = 0

nombreEstacionMaxima = ""
temperaturaMinima = 10**6

nombreEstacionMinima = ""
temperaturaMaxima = 0

#LA ULTIMA LINEA SOLO CONTIENE LA PALABRA "fin"
while(linea != "fin"):
    datos = linea.split(",")
    nombreDeEstacion = datos[0]
    try:
        temperatura = float(datos[1])
    except:
        print("El valor ingresado para [Temperatura] no es un valor numérico.")
        linea = input("Ingresar en orden: Nombre de estación, Temperatura, Humedad:  ")
        continue
    try:
        humedad = float(datos[2])
    except:
        print("El valor ingresado para [Humedad] no es un valor numérico.")
        linea = input("Ingresar en orden: Nombre de estación, Temperatura, Humedad:  ")
        continue

    #CONTADORES
    sumaTemperaturas += temperatura
    sumaHumedades += humedad
    cantidadDeElementos += 1

    #MINIMA/MAXIMA
    if(temperatura < temperaturaMinima):
        temperaturaMinima = temperatura
        nombreEstacionMinima = nombreDeEstacion
    if(temperatura > temperaturaMaxima):
        temperaturaMaxima = temperatura
        nombreEstacionMaxima = nombreDeEstacion

    #En caso de que alguna línea tenga temperatura por encima de los 33 grados celcius
    #y una humedad por encima del 85 %, se debe imprimir una alerta por pantalla
    #REDY
    if(temperatura > 33 and humedad > 85):
        print("Alerta en:",nombreDeEstacion," | DATOS: -Temperatura:",temperatura,"-Humedad:",humedad+"%")



    linea = input("Ingresar en orden: Nombre de estación, Temperatura, Humedad:  ")


#Una vez que se finalice la lectura de los datos, si el promedio de las temperaturas
#está por encima de 30 grados y el promedio de la humedad por debajo del 40%, se
#debe lanzar una alerta de temporada de incendios. 
if(cantidadDeElementos != 0):
    promedioTemperaturas = (sumaTemperaturas)/cantidadDeElementos
    promedioHumedades = (sumaHumedades)/cantidadDeElementos

    if(promedioTemperaturas > 30 and promedioHumedades < 40):
        print("ES TEMPORADA DE INCENDIOS!!!")

    #Además, se debe imprimir el promedio de las temperaturas, 
    # la temperatura máxima, la mínima y las estaciones donde se alcanzaron.
    print("Promedio de Temperaturas:",promedioTemperaturas)
    print("Temperatura Máxima alcanzada: ", "-Nombre de Estación:",nombreEstacionMaxima,": -Temperatura:",temperaturaMaxima)
    print("Temperatura Mínima alcanzada: ", "-Nombre de Estación:",nombreEstacionMinima,": -Temperatura:",temperaturaMinima)
else:
    print("No se ingresaron elementos.")
