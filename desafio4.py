# (C) RODRIGO JIMÉNEZ 2020 GPLv3
# ES DECIR LA COPIA DIRECTA DE ESTE CÓDIGO ES ILEGAL Y PENALIZADA POR LEY
# CUALQUIER COPIA QUE PERJUDIQUE DIRECTAMENTE A QUIEN PUBLICA ORIGINALMENTE ESTE CODIGO
# SERÁ INVESTIGADA Y SE TOMARÁN ACCIONES LEGALES CORRESPONDIENTES.

###################################################################################

#Desafío de Rodrigo Jiménez y Leandro Vergara







#Cada paciente (in pacientes) = [hora,nombre,puls,presion,temp,resp, STATUS]
pacientes = []
pacientesHorarioInhabil = 0
pacientesGraves = 0
pacientesCriticos = 0
pacientesEstablesHoraPunta = 0
pacientesEnBloque = [0,0,0,0,0,0,0,0,0,0,0,0] #Rangos desde las 00:00 hasta las 23:59
pulsosAnormalesBloque = [0,0,0,0,0,0,0,0,0,0,0,0] #Solo se guardarán los pacientes con pulso anormal


#def es para defninir    ->   def f(x):
#sino piensa que estas llamando la funcion, ej: y = f(x) <- si f(x) tiene un return
def convertirHora(horaDecimal):

    horaOutput = int(horaDecimal) #La hora sin minut0s
    minutos = int((horaDecimal - horaOutput)*60) # devuelve el porcentaje de minutos que han pasado * 60, es decir los minutos
    horaEstandar = f"{str(horaOutput).zfill(2)}:{str(minutos).zfill(2)}" 
    return (horaEstandar)

def clasificarBloques(hora):

    idBloque = -1

    if(0 <= hora < 2):
        idBloque = 0
    elif(2 <= hora < 4):
        idBloque = 1
    elif(4 <= hora < 6):
        idBloque = 2
    elif(6 <= hora < 8):
        idBloque = 3
    elif(8 <= hora < 10):
        idBloque = 4
    elif(10 <= hora < 12):
        idBloque = 5
    elif(12<= hora < 14):
        idBloque = 6
    elif(14 <= hora < 16):
        idBloque = 7
    elif(16 <= hora < 18):
        idBloque = 8
    elif(18 <= hora < 20):
        idBloque = 9
    elif(20 <= hora < 22):
        idBloque = 10
    elif(22 <= hora < 24):
        idBloque = 11
    return idBloque
    
def BloqueMasPacientes(listaBloques):

    cantidadMasPacientes = max(listaBloques)
    bloquesConIndice = []

    for i, bloque in enumerate(listaBloques):
        #Chequea recursivamente por los bloques
        #agrega a los bloques con respectivo indice de horario
        #Solo si es que son los que tienen más pacientes
        #Es decir, si hay mas de un bloque con mayor cantidad de pacientes, es agregado a la lista.
        if(bloque == cantidadMasPacientes):
            bloqueAgregar = [i,bloque]
            bloquesConIndice.append(bloqueAgregar)
    
    return bloquesConIndice

def ClasificarPaciente(paciente):

    actualStatus = 0 # 0 == error

    #PULSO
    if(paciente[2] < 30 or paciente[2] > 150):
        #Critico
        actualStatus = 1
    elif(paciente[2] < 50 or paciente[2] > 120):
        #Grave
        actualStatus = 2
    elif(paciente[2] < 60 or paciente[2] > 90):
        #Leve
        actualStatus = 3
    elif(60 < paciente[2] < 90):
        #Estable
        actualStatus = 4

    #PRESION
    if(paciente[3] < 40 or paciente[3] > 180):
        #critico
        status = 1
        if(status <= actualStatus):
            actualStatus = status
    elif(paciente[3] < 60 or paciente[3] > 150):
        #grave
        status = 2
        if(status <= actualStatus):
            actualStatus = status
    elif(paciente[3] < 90 or paciente[3] > 120):
        #leve
        status = 3
        if(status <= actualStatus):
            actualStatus = status
    elif(90 < paciente[3] < 120):
        #estable
        status = 4
        if(status <= actualStatus):
            actualStatus = status

    #Temperatura
    if(paciente[4] >= 42):
        #Critico
        status = 1
        if(status <= actualStatus):
            actualStatus = status
    elif(paciente[4] >= 40.5):
        #Grave
        status = 2
        if(status <= actualStatus):
            actualStatus = status
    elif(paciente[4] >= 37.3):
        #Leve
        status = 3
        if(status <= actualStatus):
            actualStatus = status
    elif(36.6 < paciente[4] < 37.2):
        #Estable
        status = 4
        if(status <= actualStatus):
            actualStatus = status

    #Respiracion
    if(paciente[5] < 15 or paciente[5] > 20):
        #Grave
        status = 2
        if(status <= actualStatus):
            actualStatus = status
    elif(15 < paciente[5] < 20):
        #Estable
        status = 4
        if(status <= actualStatus):
            actualStatus = status

    return actualStatus

def ProcesarArchivo():

    global pacientesCriticos
    global pacientesGraves

    archivo = open("pacientes.csv" , "r")
    for i, linea in enumerate(archivo): #enumerate() para saber en que linea estamos, con la variable i
        if(i > 0):  #La primera linea contiene los nombres de los datos
            paciente = linea.strip().split(";")
            paciente[0] = float(paciente[0].replace(",","."))
            paciente[2] = float(paciente[2].replace(",","."))#pulso
            paciente[3] = float(paciente[3].replace(",","."))#presion
            paciente[4] = float(paciente[4].replace(",","."))#temp
            paciente[5] = float(paciente[5].replace(",","."))#respiración
            paciente.append(ClasificarPaciente(paciente)) # 1 critico; 2 grave; 3 medio; 4 estable  
            pacientes.append(paciente) #El status se guarda en el elemento 7
            if(paciente[6] == 1):
                #Si nuestro paciente tiene status = critico
                pacientesCriticos += 1
            elif(paciente[6] == 2):
                #Si nuestro paciente está en estado grave
                pacientesGraves += 1
    archivo.close()    

def ProcesarPacientes():
    global pacientesEstablesHoraPunta
    global pacientesHorarioInhabil

    for paciente in pacientes:
        if(paciente[6] == 4 and 18 <= paciente[0] < 21): # Estable y en hora punta
            pacientesEstablesHoraPunta += 1
            

        #Chequear horas
        bloquePaciente = clasificarBloques(paciente[0])
        pacientesEnBloque[bloquePaciente] += 1
        if not (bloquePaciente < 0 or bloquePaciente > 11):
            if(bloquePaciente <= 3 or bloquePaciente >= 10):
                pacientesHorarioInhabil += 1
        
        if not (60 < paciente[2] < 90):
            #si no es (pulso Estable)
            pulsosAnormalesBloque[bloquePaciente] += 1
            
        



ProcesarArchivo()
ProcesarPacientes()

#CANTIDAD PACIENTES HORARION INHABIL
print(f"Cantidad de pacientes llegados en horario inhábil: {pacientesHorarioInhabil}\n")

# % de pacientes graves y criticos
porcentajeGraves =  (pacientesGraves / len(pacientes)) * 100
porcentajeCriticos = (pacientesCriticos / len(pacientes)) * 100
print(f" - Porcentaje de pacientes graves: {porcentajeGraves}% \n - Porcentaje de pacientes críticos: {porcentajeCriticos}% \n")

#Cantidad de personas estables en horario punta
print(f"Cantidad de personas estables en hora punta: { pacientesEstablesHoraPunta } \n")

#Rango de horario con más pacientes
rangosMasPacientes = BloqueMasPacientes(pacientesEnBloque)
print(f"Rango de horario con más pacientes: ")
#Mostrar los rangos que tiene mas pacientes obtenidos con la funcion
for rango in rangosMasPacientes:
    horaInicio = (rango[0]*2) -2
    horaTermino = rango[0]*2
    print(f" [{convertirHora(horaInicio)} - {convertirHora(horaTermino)}]: {rango[1]} pacientes.")

#Rango de horario con más pacientes de pulso anormal
rangosMasPulso = BloqueMasPacientes(pulsosAnormalesBloque)
print(f"Rango de horario con más pacientes con pulso anormal: ")
#Mostrar los rangos que tiene mas pacientes obtenidos con la funcion
for rango in rangosMasPulso:
    horaInicio = (rango[0]*2) -2
    horaTermino = rango[0]*2
    print(f" [{convertirHora(horaInicio)} - {convertirHora(horaTermino)}]: {rango[1]} pacientes con pulso anormal.")


