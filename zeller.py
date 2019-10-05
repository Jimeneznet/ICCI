#Modulo Zeller por: Rodrigo Jiménez para uso en desafío_2

#modulo = str(-2 % 7)   #En la página de wikipedia dice que muchos lenguajes de programación devuelven esta operación con un -2, y que por ende se usa una modificación
#print(modulo)          #Sin embargo, comprobé que python devuelve 5, que es lo que devuelve la definición matemática de la operación módulo

                    #NOTA DE JIMENEZ DE UN FUTURO PROXIMO: al final abajo había una mejor implementación de software, que funciona perfectamente en python.

#Así que esta función está programada con la versión original del algoritmo.
def CalendarioGregoriano(diaDelMes, mes, año):
    diaDelMes = int(diaDelMes)
    mes = int(mes)
    año = int(año)
    if(mes < 3):
        año -= 1    #Esta es la parte de la implementación que nos permite usar Zeller sin las variables J y K

    output = ((diaDelMes)    +  (int((13*(mes + 1)) / 5)) + (año) + (int(año/4)) - (int(año/100)) + (int(año/400))) % 7 #El exceso de paréntesis es solo trastorno obsesivo compulsivo.
    output = ((output+5)%7)+1         #Descomentar esta linea hará que los resultados sean segun el estándar de la ISO (lunes = 1, martes = 2, etc)
    return output

#DE ACA PARA ABAJO ESCRIBE, SOLO PUEDES LLAMAR FUNCIONES DEFINIDAS PREVIAMENTE (lenguaje interpretado po perrito)

#Ah, y por cierto, cambia lo que quieras, pero la operación de zeller ya esta lista.


#param1 = int(input("Dia del Mes"))
#param2 = int(input("Mes"))
#param3 = int(input("Año"))

#diasemana = CalendarioGregoriano(param1,param2,param3) #Asi puedes llamar la función, en cualquier del programa, 

#print(diasemana)

#Tu pega: separar las variables de las lineas (split) e ingresarlas en la función

countL = 0
countM = 0
countI = 0
countJ = 0
countV = 0
countS = 0
countD = 0

lineas = open("fechas.txt").readlines() #Crea una lista con todas las lineas de "fechas.txt"
for linea in lineas:
    linea = linea.strip().split("/")
    diaDeSemana = CalendarioGregoriano(linea[0],linea[1],linea[2])
	
    if(diaDeSemana == 1):
	    #lunes
        countL += 1
    if(diaDeSemana == 2):
	    #martes
        countM += 1
    if(diaDeSemana == 3):
	    #miercoles
        countI += 1
    if(diaDeSemana == 4):
	    #jueves
        countJ += 1
    if(diaDeSemana == 5):
	    #viernes
        countV += 1
    if(diaDeSemana == 6):
	    #sabado
        countS += 1
    if(diaDeSemana == 7):
	    #domingo
        countD += 1


      
diasMayores = ""
diasMenores = ""  
        
if countL >= countM and countL >= countI and countL >= countJ and countL >= countV and countL >= countS and countL >= countD:
    diasMayores += " Lunes"
elif countL <= countM and countL <= countI and countL <= countJ and countL <= countV and countL <= countS and countL <= countD:
    print("menor: lunes")


if countM >= countL and countM >= countI and  countM >= countJ and countM >= countV and countM >= countS and countM >= countD:
    diasMayores += " Lunes"
elif countM <= countL and countM <= countI and countM <= countJ and countM <= countV and countM <= countS and countM <= countD:
    print("menor: martes")   


if countI >= countM and countI >= countL and countI >= countJ and countI >= countV and countI >= countS and countI >= countD:
    diasMayores += " Lunes"
elif countI <= countM and countI <= countL and countI <= countJ and countI <= countV and countI <= countS and countI <= countD:
    print("menor: miercoles")   


if countJ >= countM and countJ >= countI and countJ >= countL and countJ >= countV and countJ >= countS and countJ >= countD:
    diasMayores += " Lunes"
elif countJ <= countM and countJ <= countI and countJ <= countL and countJ <= countV and countJ <= countS and countJ <= countD:
    print("menor: jueves")   


if countV >= countM and countV >= countI and countV >= countJ and countV >= countL and countV >= countS and countV >=countD:
    print("mayor: viernes")
elif countV <= countM and countV <= countI and countV <= countJ and countV <= countL and countV <= countS and countV <= countD:
    print("menor: viernes")   


if countS >= countM and countS >= countI and countS >= countJ and countS >= countV and countS >= countL and countS >= countD:
    print("mayor: sabado")
elif countS <= countM and countS <= countI and countS <=countJ and countS <= countV and countS <= countL and countS <= countD:
    print("menor: sabado")   


if countD >= countM and countD >= countI and countD >= countJ and countD >= countV and countD >= countS and countD >= countL:
    print("mayor: domingo")
elif countD <= countM and countD <= countI and countD <= countJ and countD <= countV and countD <= countS and countD <= countL:
    print("menor: domingo")            


        
total = countL + countM + countI + countJ + countV + countS + countD
porcentajeDomingos = (countD/total)*100
print(porcentajeDomingos)
