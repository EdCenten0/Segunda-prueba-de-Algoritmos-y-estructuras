import os

# Se crea una funcion que busca una asignatura en funcion de su codigo
def buscar(pooPara, calculo2Para, tallerRedaccionPara, algotitmosEstructurasPara, principiosRedesPara):
    os.system("cls")
    opcion = input("Ingrese el codigo de la clase que desea buscar: ")
    if(opcion == "B126"):
        print("POO".center(100))
        print(pooPara)
        os.system("pause")
    elif(opcion == "B112"):
        print("Calculo 2".center(100))
        print(calculo2Para)
        os.system("pause")
    elif(opcion == "B114"):
        print("Taller de Redaccion".center(100))
        print(tallerRedaccionPara)
        os.system("pause")
    elif(opcion == "B124"):
        print("Algoritmos y estructuras de datos".center(100))
        print(algotitmosEstructurasPara)
        os.system("pause")
    elif(opcion == "0040"):
        print("Pricipios de redes informáticas ".center(100))
        print(principiosRedesPara)
        os.system("pause")