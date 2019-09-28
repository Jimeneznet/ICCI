#Modulo Zeller por: Rodrigo Jiménez para uso en desafío_2

#modulo = str(-2 % 7)   #En la página de wikipedia dice que muchos lenguajes de programación devuelven esta operación con un -2, y que por ende se usa una modificación
#print(modulo)          #Sin embargo, comprobé que python devuelve 5, que es lo que devuelve la definición matemática de la operación módulo

                    #NOTA DE JIMENEZ DE UN FUTURO PROXIMO: al final abajo había una mejor implementación de software, que funciona perfectamente en python.

#Así que esta función está programada con la versión original del algoritmo.
def CalendarioGregoriano(diaDelMes, mes, año):
    if(mes < 3):
        año -= 1    #Esta es la parte de la implementación que nos permite usar Zeller sin las variables J y K

    output = ((diaDelMes)    +  (int((13*(mes + 1)) / 5)) + (año) + (int(año/4)) - (int(año/100)) + (int(año/400))) % 7 #El exceso de paréntesis es solo trastorno obsesivo compulsivo.
    #output = ((output+5)%7)+1         #Descomentar esta linea hará que los resultados sean segun el estándar de la ISO (lunes = 1, martes = 2, etc)
    return output

#DE ACA PARA ABAJO ESCRIBE, SOLO PUEDES LLAMAR FUNCIONES DEFINIDAS PREVIAMENTE (lenguaje interpretado po perrito)

#Ah, y por cierto, cambia lo que quieras, pero la operación de zeller ya esta lista.


param1 = int(input("Dia del Mes"))
param2 = int(input("Mes"))
param3 = int(input("Año"))

diasemana = CalendarioGregoriano(param1,param2,param3) #Asi puedes llamar la función, en cualquier del programa, 

print(diasemana)

#Tu pega: separar las variables de las lineas (split) e ingresarlas en la función
