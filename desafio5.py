import numpy as np

paises = dict()

rangosEtariosGlobal = np.zeros(10, dtype=int)

contagiosPorDia = np.empty(0,dtype=int) #Una lista de ints vacíos.
diaActual = 0

def clasificarRangoEtario(edad):
    #Esta función nos clasifica un paciente en nuestros rangos etarios
    #devuelve un índice que corresponde al índice en nuestra lista de rangos. 
    #Nuestra lista de rangos tiene de 10 rangos, desde el 1 al 100.

    try:
        edad = int(edad) #Para evitar errores de tipo.
        if(edad > 0):
            edad += -1 #Para evitar errores de clasificación, si no, un paciente con 10 años entrará en el rango [1], de 11 a 20 años.
        rango = int(edad/10) #es decir, nuestra edad ahora es un decimal, y luego es truncado por int.
        return rango #eso significa que si el paciente tiene 10 años, estara en el rango 0.
    except ValueError:
        print("ATENCION: error procesando rango etario de paciente.")
        print("ATENCION: ¿Es el tipo de dato que recibe la función correcto?.")

def RangoEtarioContagioPais(pais):
    rangoEtarioPais = np.zeros_like(rangosEtariosGlobal)
    for paciente in paises[pais]:
        rangoEtarioPais[clasificarRangoEtario(paciente[4])] += 1
    return rangoEtarioPais

def DesplegarRangosEtarios(rangos):

    for i in range(len(rangos)):
        print(f"\t[{(i+1)} - {((i+1)*10)-1}]: {rangos[i]} contagios.")

def ProcesarArchivo(ruta):
    archivo = open(ruta)

    global contagiosPorDia
    global rangosEtariosGlobal
    global paises
    global diaActual

    try:
        for linea in archivo:
            l = linea.strip().split(";")
            l[1] = int(l[1]) # DIA
            l[2] = l[2].upper() #LOS PAISES SE GUARDAN EN MAYUSCULAS!
            l[3] = l[3].upper() #El SEXO TAMBIEN
            l[4] = int(l[4])  # EDAD
            rangosEtariosGlobal[clasificarRangoEtario(l[4])] += 1
            if((l[1]+1) > len(contagiosPorDia)): #Al dia del paciente se le suma uno, debido a que el dia 1 implica una lista de dos términos.
                diferencia = (l[1]+1) - len(contagiosPorDia)
                contagiosPorDia = np.pad(contagiosPorDia,(0,diferencia))

            #Sin importar el día, después de el código anterior, el día deberia tener un índice correspondiente
            contagiosPorDia[l[1]] += 1

            if(l[2] in paises):
                #print(f"Existe pais {l[2]}")
                paises[l[2]].append(l)
            else:
                paises[l[2]] = [l]
        
        archivo.close()
        diaActual = len(contagiosPorDia)
        return True
    except ValueError:
        print("Se produjo un error en el procesamiento del archivo.\nChequee la integridad de la estructura de datos.")
        return False

def IngresarPacienteNuevo():
    
    idValido = False
    id_paciente = 0
    while not idValido:
        try:
            id_paciente = int(input("Ingrese el identificador del paciente: ")) or False
            if not (id_paciente == False):
                idValido = True
            else:
                print(" - Inténtelo de nuevo.")
        except ValueError:
            print(" - Ha ingresado un valor no admitido. Solo se admiten números.")        

    paisValido = False
    pais_paciente = ""
    while not paisValido:
        pais_paciente = input("Ingrese el país del paciente: ").upper() or False
        if not (pais_paciente == False):
            paisValido = True
        else:
            print(" - Inténtelo de nuevo.")

    sexoValido = False
    sexo_paciente = ""
    while not sexoValido:
        sexo_paciente = input("Ingrese el sexo del paciente: ").upper() or False
        if(sexo_paciente == "MASCULINO" or sexo_paciente == "FEMENINO"):
            sexoValido = True
        else:
            print(" - Inténtelo de nuevo. Solo puede ingresar 'MASCULINO' o 'FEMENINO'")

    edadValida = False
    edad_paciente = 0
    while not edadValida:
        try:
            edad_paciente = int(input("Ingrese edad del paciente: ")) or False
            if not (edad_paciente < 0 or edad_paciente == False):
                edadValida = True
            else:
                print(" - Inténtelo de nuevo.")
        except ValueError:
            print(" - Ha ingresado un valor no admitido. Solo se admiten números.")    

    print(f" - PACIENTE NUEVO - ")
    print(f"Identificador: {id_paciente}")
    print(f"Dia de ingreso: {len(contagiosPorDia)}")
    print(f"Pais: {pais_paciente}")
    print(f"Sexo: {sexo_paciente}")
    print(f"Edad: {edad_paciente}")

    paciente = [id_paciente,diaActual,pais_paciente,sexo_paciente,edad_paciente]

    agregarPacienteValido = False
    while not agregarPacienteValido:
        respuestaAgregarPaciente = input("¿Desea agregar al paciente? (Si/No): ").upper()
        if(respuestaAgregarPaciente == "SI"):
            if(pais_paciente in paises):
                paises[pais_paciente].append(paciente)
            else:
                paises[pais_paciente] = [paciente]
            
            rangoEtarioPaciente = clasificarRangoEtario(edad_paciente)
            rangosEtariosGlobal[rangoEtarioPaciente] += 1

            if(diaActual+1 == len(contagiosPorDia) ):
                contagiosPorDia[diaActual] += 1
            else:
                np.append(contagiosPorDia,1)

            print(f"Se ha agregado el paciente {id_paciente}.")
            agregarPacienteValido = True
        elif(respuestaAgregarPaciente == "NO"):
            print(f"Se ha descartado el paciente {id_paciente}.")
            agregarPacienteValido = True
        else:
            print(" - Ingrese una respuesta válida.")

    pacienteNuevoValido = False
    agregarNuevoPaciente = False
    while not pacienteNuevoValido:
        respuestaPacienteNuevo = input("¿Desea ingresar un nuevo paciente? (Si/No): ").upper()
        if(respuestaPacienteNuevo == "SI"):
            agregarNuevoPaciente = True
            pacienteNuevoValido = True
        elif(respuestaPacienteNuevo == "NO"):
            agregarNuevoPaciente = False
            pacienteNuevoValido = True
        else:
            print(" - Ingrese una respuesta válida.")

    if(agregarNuevoPaciente):
        IngresarPacienteNuevo()
    


def DatosPaisMasContagios():
    paisConMasContagiados = max(paises, key=lambda x:len(paises[x]))
    print(f"El país con más contagios es: {paisConMasContagiados} - {len(paises[paisConMasContagiados])} contagios.")
    print(f"Contagiados por rango etario:")
    #rangosEtariosPais = RangoEtarioContagioPais(paisConMasContagiados) #Esta función solía desplegar el rango etario también, pero complicaría la revisión del codigo
    #DesplegarRangosEtarios(rangosEtariosPais)

def RangoEtarioMasContagiado():
    rangoMasContagiado = max(rangosEtariosGlobal)
    indicesRangoContagiado = np.where(rangosEtariosGlobal == rangoMasContagiado)
    print(f"Rangos etarios con más contagios:")
    for i in indicesRangoContagiado[0]:
        print(f"\tRango {i} [{i*10} - {((i+1)*10)-1}]: {rangoMasContagiado} contagios. ")

def ContagiosPorSexoChina():
    hombresInfectadosChina = 0
    mujeresInfectadasChina = 0
    for paciente in paises["CHINA"]:
        if(paciente[3] == "MASCULINO"):
            hombresInfectadosChina += 1
        elif(paciente[3] == "FEMENINO"):
            mujeresInfectadasChina += 1

    print(f"En China existen:\n\t - {hombresInfectadosChina} Hombres infectados.\n\t - {mujeresInfectadasChina} Mujeres infectadas.")

def diaConMasContagios():
    #Era necesario? Podemos usar la funcion max()
    masContagios = max(contagiosPorDia)
    indicesDiasContagios = np.where(contagiosPorDia == masContagios)
    print(f"Los días con más contagios ({masContagios} contagios)")
    for i in indicesDiasContagios[0]:
        print(f"\tEl dia {i}, con {masContagios} nuevos casos.")
    return indicesDiasContagios[0]

ProcesarArchivo("COVID19_DATA.txt")
IngresarPacienteNuevo()

print("\n-------------\n")

DatosPaisMasContagios()

print("\n-------------\n")

RangoEtarioMasContagiado()

print("\n-------------\n")

print("Rango etario de CHINA:")
DesplegarRangosEtarios(RangoEtarioContagioPais("CHINA"))

print("\n-------------\n")

ContagiosPorSexoChina()

print("\n-------------\n")

diaConMasContagios()

pais = input("Ingrese país: ").upper()
DesplegarRangosEtarios(RangoEtarioContagioPais(pais))