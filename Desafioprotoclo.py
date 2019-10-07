# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:44:28 2019

@author: symac
"""
universidadesReprobadas = 0
nombreUniversidad =  input("Ingrese el nombre de la universidad: ")
while(nombreUniversidad != "fin"):
    try:
        unidadesDeRevision = int(input("Cantidad de unidades que revisarán el protocolo: "))
    except:
        print("No es un numero")
        continue
    
    totalObservacionesPositivas = 0
    totalObservacionesNegativas = 0
    
    for n in range(0,unidadesDeRevision):
        nombreUnidad = input("Ingrese el nombre de la unidad: ")
        observacionesPositivas = int(input("Cantidad de observaciones positivas"))
        observacionesNegativas = int(input("Cantidad de observaciones negativas"))
        totalObservacionesUnidad = observacionesPositivas + observacionesNegativas
        print("Porcentaje de Obervaciones Positivas de la unidad: ", (observacionesPositivas/totalObservacionesUnidad)*100)
        print("Porcentaje de Obervaciones Negativas de la unidad: ",(observacionesNegativas/totalObservacionesUnidad)*100)
        
        
        totalObservacionesPositivas += observacionesPositivas
        
        totalObservacionesNegativas += observacionesNegativas
    
    
    totalDeObservacionesUniversidad = (totalObservacionesPositivas + totalObservacionesNegativas)
    
    porcentajeDeAprobacion = (totalObservacionesPositivas/totalDeObservacionesUniversidad)*100
    
    aprobacion = ""
    
    if(porcentajeDeAprobacion >= 70):
        aprobacion = "APROBADO"
    else:
        aprobacion = "REPORTADO"
        universidadesReprobadas += 1
    
    print("Universidad: ", nombreUniversidad," Aprobación: ", aprobacion)
        
    print("Observaciones +  de univ : " + str(totalObservacionesPositivas))
    print("Observaciones -  de univ : " + str(totalObservacionesNegativas))
    
    nombreUniversidad = input("Ingrese el nombre de la universidad: ")
    
print("Universidades sin protocolo: ", universidadesReprobadas)