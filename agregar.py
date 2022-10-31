import os

# Se crea una función que ingresa la nota del estudiante
def agregar(pooPara, calculo2Para, tallerRedaccionPara, algotitmosEstructurasPara, principiosRedesPara):
    os.system("cls")
    print("POO - B126".center(100))
    for i in range(0,3):
        pooAux = int(input("Ingrese el acumulado " + str(i+1) + ": "))
        pooPara.append(pooAux)

    print("Calculo 2 - B112".center(100))
    for i in range(0,3):
        calcAux = int(input("Ingrese el acumulado " + str(i+1) + ": "))
        calculo2Para.append(calcAux)

    print("Taller de Redaccion - B114".center(100))
    for i in range(0,3):
        RedacAux = int(input("Ingrese el acumulado " + str(i+1) + ": "))
        tallerRedaccionPara.append(RedacAux)

    print("Algoritmos y estructuras de datos - B124".center(100))
    for i in range(0,3):
        AlgAux = int(input("Ingrese el acumulado " + str(i+1) + ": "))
        algotitmosEstructurasPara.append(AlgAux)

    print("Pricipios de redes informáticas - 0040".center(100))
    for i in range(0,3):
        priAux = int(input("Ingrese el acumulado " + str(i+1) + ": "))
        principiosRedesPara.append(priAux)

    