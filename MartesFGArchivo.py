archivo = open("alumnos.txt")
linea = archivo.readline()

cantidadAlumnos = 0 
AlumnosPrograPrimeraOSegunda = 0 # requisito 1
cantidadAlumnosCalculo = 0  
AlumnosCalculoCuartaOMas = 0 # requisito 3

cantidadAlumnosRequisito2 = 0 # requisito 2

while(linea != ""):
    print(linea)
    datos = linea.strip().split(",")
    nombre = datos[0]
    asignatura = datos[1]
    oportunidad = int(datos[2])
    cantidadAlumnos += 1

    

    #Requisito 1
    if(asignatura == "PROGRAMACION" and oportunidad > 0 and oportunidad < 3):
        AlumnosPrograPrimeraOSegunda += 1
    
    #Requisito3
    if(asignatura == "CALCULO II"):
        cantidadAlumnosCalculo += 1
        if(oportunidad >= 4):
            AlumnosCalculoCuartaOMas += 1

    ciudad = input("Indique la ciudad de residencia del alumno: ")
    cantidadDeHijos = int(input("Indique la cantidad de hijos del alumno: "))

    if(ciudad == "ANTOFAGASTA" or ciudad == "CALAMA"):
        if(cantidadDeHijos >= 1 or cantidadDeHijos <= 3):
            cantidadAlumnosRequisito2 += 1

    linea = archivo.readline()


print("Cantidad de alumnos cursando programación por primera o segunda vez:",AlumnosPrograPrimeraOSegunda)
if(cantidadAlumnos != 0):
    print("Porcentaje de alumnos que son de Antofagasta o Calama, y tienen entre uno y tres hijos: ", str((cantidadAlumnosRequisito2/cantidadAlumnos)*100)+"%")
if(cantidadAlumnosCalculo != 0):
    print("Porcentaje de alumnos de Calculo II, que cursan en su cuarta o mayor oportunidad: ", str((AlumnosCalculoCuartaOMas/cantidadAlumnosCalculo)*100)+"%")

