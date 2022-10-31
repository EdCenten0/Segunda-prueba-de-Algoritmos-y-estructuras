import os


# Se crea una funcion que imprime la nota final de cada asignatura y el promedio del estudiante
def imprimirDatos(pooPara, calculo2Para, tallerRedaccionPara, algotitmosEstructurasPara, principiosRedesPara):
    print("Notas de POO: ")
    acumuladoPOO=0
    for i in range(0,3):
        acumuladoPOO = acumuladoPOO + pooPara[i]
    print("La nota final es: " + str(acumuladoPOO))
    
    print("Notas de Cálculo 2: ")
    acumuladoCalc=0
    for i in range(0,3):
        acumuladoCalc = acumuladoCalc + calculo2Para[i]
    print("La nota final es: " + str(acumuladoCalc))

    print("Notas de Taller de redacción: ")
    acumuladoTaller=0
    for i in range(0,3):
        acumuladoTaller = acumuladoTaller + tallerRedaccionPara[i]
    print("La nota final es: " + str(acumuladoTaller))

    print("Notas de Algoritmos y estructuras de datos: ")
    acumuladoAlg=0
    for i in range(0,3):
        acumuladoAlg = acumuladoAlg + algotitmosEstructurasPara[i]
    print("La nota final es: " + str(acumuladoAlg))

    print("Notas de Principios de redes informáticas: ")
    acumuladoRedes=0
    for i in range(0,3):
        acumuladoRedes = acumuladoRedes + principiosRedesPara[i]
    print("La nota final es: " + str(acumuladoRedes))

    promedio = (sum(pooPara) + sum(calculo2Para) + sum(tallerRedaccionPara) + sum(algotitmosEstructurasPara) + sum(principiosRedesPara)) / 15
    print("El promedio final es de " + str(promedio))
    
    os.system("pause")
    
    