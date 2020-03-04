#Estas variables contienen los pacientes de cada clínica, después de procesar los archivos
pacientesC1 = []
pacientesC2 = []
pacientesC3 = []

cantidadPacientesNuevosC1 = 0
cantidadPacientesNuevosC2 = 0
cantidadPacientesNuevosC3 = 0

#Esta función trasladará pacientes desde las clínicas según coresponda su edad
def trasladar_pacientes():

    archivo1 = open("1.txt", "r")
    for linea in archivo1:
        l = linea.strip().split(",")
        l[1] = int(l[1])
        if( l[1] < 10 ):
            #Nuestro paciente debe ser trasladado a la clínica 2
            pacientesC2.append(l)
        else:
            pacientesC1.append(l)
    
    archivo2 = open("2.txt", "r")
    for linea in archivo2:
        l = linea.strip().split(",")
        l[1] = int(l[1])
        pacientesC2.append(l)
    
    archivo3 = open("3.txt", "r")
    for linea in archivo3:
        l = linea.strip().split(",")
        l[1] = int(l[1])
        if( l[1] < 10 ):
            #Nuestro paciente debe ser trasladado a la clínica 2
            pacientesC2.append(l)
        else:
            pacientesC3.append(l)

    

def pacientes_rango_edad(a,b,incluirExtremos):
    #incluirExtremos = True
    pacientesEnRango = []

    if(incluirExtremos):
        for paciente in pacientesC1:
            if(int(paciente[1]) >= a and int(paciente[1]) <= b):
                pacientesEnRango.append(paciente)

        for paciente in pacientesC2:
            if(int(paciente[1]) >= a and int(paciente[1]) <= b):
                pacientesEnRango.append(paciente)

        for paciente in pacientesC3:
            if(int(paciente[1]) >= a and int(paciente[1]) <= b):
                pacientesEnRango.append(paciente)
    else:
        for paciente in pacientesC1:
            if(int(paciente[1]) > a and int(paciente[1]) < b):
                pacientesEnRango.append(paciente)

        for paciente in pacientesC2:
            if(int(paciente[1]) > a and int(paciente[1]) < b):
                pacientesEnRango.append(paciente)

        for paciente in pacientesC3:
            if(int(paciente[1]) > a and int(paciente[1]) < b):
                pacientesEnRango.append(paciente)

    return pacientesEnRango

#Esta función es para cuando sabemos la clinica a la que entra el paciente
def ingresar_paciente(clinica):
    pacienteValido = False
    nombrePaciente = False
    edadPaciente = False

    while pacienteValido == False:
        nombrePaciente = input("Ingrese el nombre del paciente: ") or False
        try:
            edadPaciente = int(input("Ingrese la edad del paciente: ")) or False
        except ValueError:
            edadPaciente = False
            print("No ha ingresado una edad válida, asegúrese de solo ingresar números.\n")
        if(nombrePaciente == False or edadPaciente == False):
            pacienteValido = False
            print("Hubo un error al ingresar el paciente.\n")
        else:
            pacienteValido = True
        continue
            
    
    paciente = [nombrePaciente,edadPaciente]

    if(clinica == 1):
        pacientesC1.append(paciente)
        global cantidadPacientesNuevosC1 #El global se agrega para que el valor se cambie también fuera de la función, o da error.
        cantidadPacientesNuevosC1 += 1
    elif(clinica == 2):
        pacientesC2.append(paciente)
        global cantidadPacientesNuevosC2 #El global se agrega para que el valor se cambie también fuera de la función, o da error.
        cantidadPacientesNuevosC2 += 1
    elif(clinica == 3):
        pacientesC3.append(paciente)
        global cantidadPacientesNuevosC3 #El global se agrega para que el valor se cambie también fuera de la función, o da error.
        cantidadPacientesNuevosC3 += 1
    else:
        print("Error ingresando a paciente: Clínica no válida.")

#Si no sabemos la clinica, esta función pregunta y asigna de manera correspondiente
def ingresar_a_clinica():
    clinicaValida = False
    clinica = False 

    while clinicaValida == False:
        try:
            clinica = int(input("Ingrese la clínica que corresponde al paciente (1, 2 ó 3): ")) or False
            if(clinica < 1 or clinica > 3):
                clinica = False
        except ValueError:
            clinica = False
            print("No ha ingresado una clinica válida, asegúrese de solo ingresar números.\n")
        if(clinica == False):
            clinicaValida = False
            print("Hubo un error al ingresar la clínica.\n")
        else:
            clinicaValida = True
            ingresar_paciente(clinica)

def menu():
    #Esto es solamente para mas funcionalidad.
    print("\n\n¿Qué desea realizar ahora?")
    opcionValida = False
    respuesta = 0
    while opcionValida == False:
        try:
            respuesta = int(input("1.- Ingresar un nuevo paciente a cualquier clínica\n2.- Buscar según el rango de edad\n3.- Mostrar la respuesta del desafío.\n4.- Salir\n - Opción: "))
            if(respuesta < 1 or respuesta > 3):
                opcionValida = False
            else:
                opcionValida = True
        except ValueError:
            print("Solo puede ingresar la opción 1, 2 ó 3. Asegurese de ingresar solamente números.")
            opcionValida = False

    if(respuesta == 1):
        ingresar_a_clinica()
    elif(respuesta == 2):

        respuestaRangoValida = False
        a = 0
        b = 0
        while respuestaRangoValida == False:
            try:
                a = int(input("Ingrese el valor mínimo: "))
                b = int(input("Ingrese el valor máximo: "))
                respuestaRangoValida = True
            except ValueError:
                print("Hubo un error procesando el rango, inténtelo de nuevo. Asegúrese de ingresar números.")
                respuestaRangoValida = False

        respuestaExtremosValida = False
        incluirExtremos = True
        while respuestaExtremosValida == False:
            respuesta = input("¿Desea incluir los extremos de los intervalos en su búsqueda? \n(Respuestas válidas: Si/No | s/n | default: Si -     ").upper() or False
            if(respuesta == "SI" or respuesta == "S" or respuesta == False): #Checkear False nos permite definir un valor para una respuesta vacía
                print(f"Se incluirán en la búsqueda los pacientes que tengan edades {a} y {b}.\n")
                incluirExtremos = True
                respuestaExtremosValida = True
            elif (respuesta == "NO" or respuesta == "N"): 
                print(f"No se incluirán en la busqueda los pacientes de edades {a} y {b}.\n")
                incluirExtremos = False
                respuestaExtremosValida = True
            else:
                print("No se ha introducido una respuesta correcta\n")
            continue
        pacientesEnRango = pacientes_rango_edad(a,b,incluirExtremos)
        for paciente in pacientesEnRango:
            print(f"{paciente[0]} | Edad: {paciente[1]}")
    
    elif(respuesta == 3):
        print("Los resultados pueden variar dependiendo de las operaciones realizadas desde el inicio del programa. \n")
        respuesta_desafio()
    
    elif(respuesta == 4):
        print("Ha cerrado el programa.")
        exit()
    
    menu()

def respuesta_desafio():

    print("Desafio 3 - Rodrigo Jiménez, Leandro Vergara.")

    #Ingresar por cada clinica
    print("\nIngresar pacientes faltantes por clínica.")
    #Clinica 1
    respuestaC1Valida = False
    while respuestaC1Valida == False:
        respuestaC1 = input("¿Desea ingresar un paciente a la clínica 1? \n (Respuestas válidas: Si/No | S/N - Default: Si)   -").upper() or False
        if(respuestaC1=="S" or respuestaC1 =="SI" or respuestaC1 == False):
            #Si se quiere agregar un paciente, volveremos a preguntar.
            ingresar_paciente(1)
        elif(respuestaC1 =="N" or respuestaC1=="NO"):
            respuestaC1Valida = True
            print("No se agregará un nuevo paciente. \n")
        else:
            respuestaC1Valida = False
            print("Hubo un error procesando su respuesta.")

    #Clinica 2
    respuestaC2Valida = False
    while respuestaC2Valida == False:
        respuestaC2 = input("¿Desea ingresar un paciente a la clínica 2? \n (Respuestas válidas: Si/No | S/N - Default: Si)   -").upper() or False
        if(respuestaC2=="S" or respuestaC2 =="SI" or respuestaC2 == False):
            #Si se quiere agregar un paciente, volveremos a preguntar.
            ingresar_paciente(2)
        elif(respuestaC2 =="N" or respuestaC2=="NO"):
            respuestaC2Valida = True
            print("No se agregará un nuevo paciente. \n")
        else:
            respuestaC2Valida = False
            print("Hubo un error procesando su respuesta.")
    
    #Clinica 3
    respuestaC3Valida = False
    while respuestaC3Valida == False:
        respuestaC3 = input("¿Desea ingresar un paciente a la clínica 3? \n (Respuestas válidas: Si/No | S/N - Default: Si)   -").upper() or False
        if(respuestaC3=="S" or respuestaC3 =="SI" or respuestaC3 == False):
            #Si se quiere agregar un paciente, volveremos a preguntar.
            ingresar_paciente(3)
        elif(respuestaC3 =="N" or respuestaC3=="NO"):
            respuestaC3Valida = True
            print("No se agregará un nuevo paciente. \n")
        else:
            respuestaC3Valida = False
            print("Hubo un error procesando su respuesta.")
    


    #Mayor cantidad de pacientes
    print("\nImprimir la(s) clínica(s) con más clientes.")
    mayorCantidadPacientes = max(len(pacientesC1),len(pacientesC2),len(pacientesC3))
    print("Clinicas con mayor cantidad de pacientes:")
    if(len(pacientesC1) == mayorCantidadPacientes):
        print(f" - La clínica 1, con {mayorCantidadPacientes} pacientes.")
    if(len(pacientesC2) == mayorCantidadPacientes):
        print(f" - La clínica 2, con {mayorCantidadPacientes} pacientes.")
    if(len(pacientesC3) == mayorCantidadPacientes):
        print(f" - La clínica 3, con {mayorCantidadPacientes} pacientes.")

    #Promedio clinica 3
    print("\nMostrar el promedio de edad de la clínica 3.")
    sumatoriaC3 = 0
    for paciente in pacientesC3:
        sumatoriaC3 += paciente[1]
    promedioC3 = (sumatoriaC3/len(pacientesC3))
    print(f"El promedio de edad de la clínica 3 es de {promedioC3} años.")

    #Pacientes entre 18 y 50, por orden alfabético.
    print("\nImprimir todos los pacientes entre 18 y 50 años (inclusivo).")
    pacientesEnRango = pacientes_rango_edad(18,50,True)
    pacientesEnRango = sorted(pacientesEnRango, key = lambda  x: x[0]) #El segundo parametro le dice a sorted() que nos ordene segun el primer elemento, en este caso el nombre
    print("Pacientes que se encuentran entre 18 y 50 años.")
    print("Nombre | Edad")
    for paciente in pacientesEnRango:
        print(f"- {paciente[0]} | {paciente[1]}")


    print("\nIndicar la cantidad de pacientes nuevos ingresados, desplegar porcentaje.")

    totalPacientes = len(pacientesC1) + len(pacientesC2) + len(pacientesC3)
    totalPacientesNuevos = cantidadPacientesNuevosC1 + cantidadPacientesNuevosC2 + cantidadPacientesNuevosC3
    porcentajeNuevosTotal = (totalPacientesNuevos/totalPacientes)*100

    porcentajeNuevosC1 = (cantidadPacientesNuevosC1/len(pacientesC1))*100
    porcentajeNuevosC2 = (cantidadPacientesNuevosC2/len(pacientesC2))*100
    porcentajeNuevosC3 = (cantidadPacientesNuevosC3/len(pacientesC3))*100
    print(f"En la clínica 1 se ingresaron {cantidadPacientesNuevosC1} pacientes nuevos, que corresponden al {porcentajeNuevosC1}% de los pacientes en dicha clínica.")
    print(f"En la clínica 2 se ingresaron {cantidadPacientesNuevosC2} pacientes nuevos, que corresponden al {porcentajeNuevosC2}% de los pacientes en dicha clínica.")
    print(f"En la clínica 3 se ingresaron {cantidadPacientesNuevosC3} pacientes nuevos, que corresponden al {porcentajeNuevosC3}% de los pacientes en dicha clínica.")
    print(f"En total se ingresaron {totalPacientesNuevos} pacientes nuevos, que corresponden al {porcentajeNuevosTotal}% de los pacientes.")

trasladar_pacientes()

respuesta_desafio()
menu()

