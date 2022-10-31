# Segunda prueba de Algoritmos y estructuras de datos B124
# Carlos Eduardo Chavarría Centeno
# Universidad Centroamericana (UCA) 
# 31/10/2022

import os
from agregar import agregar
from buscar import buscar
from imprimirDatos import imprimirDatos


# Creacion de listas para cada asignatura
poo = []
calculo2 = []
tallerRedaccion = []
algoritmosEstructuras = []
principiosRedes = []

# Se crea la función main
def main(poo, calculo2, tallerRedaccion, algoritmosEstructuras, principiosRedes):

    # Se crea un menú para todas la funciones
    opcion = 1
    while(opcion > 0 and opcion != 4):
        os.system("cls")
        print("Bienvenido al programa de acumulados de asignaturas".center(100))
        print("1. Agregar datos")
        print("2. Buscar datos")
        print("3. Imprimir datos")
        print("4. Salir")
        opcion = int(input("Que desea hacer?:\n"))
        if(opcion == 1):
            agregar(poo, calculo2, tallerRedaccion,algoritmosEstructuras, principiosRedes)
        elif(opcion == 2):
            buscar(poo, calculo2, tallerRedaccion,algoritmosEstructuras, principiosRedes)
        elif(opcion == 3):
            imprimirDatos(poo, calculo2, tallerRedaccion,algoritmosEstructuras, principiosRedes)
        elif(opcion == 4):
            print("Saliendo del programa...")
        else:
            print("Introduzca una opcion valida")
            os.system("paise")


    

main(poo, calculo2, tallerRedaccion,algoritmosEstructuras, principiosRedes)