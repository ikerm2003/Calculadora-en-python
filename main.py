import math
from colorama import Fore, Style
import time
import operator
import functools
import statistics as stat

menuOper = '''
Escoge una opción:
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Raiz cuadrada de la suma de todo, si hay mas de un número
    6) Funciones trigonométricas
    7) Funciones estadísticas
    0) Salir
Utilice el número correspondiente a su selección >>> '''  # menu para elegir las operaciones
menuTrig = '''
¿Que función trigonométrica deseas hacer con la suma de tus números?
    1) Seno
    2) Coseno
    3) Tangente
    0) Salir
Utilice el número correspondiente a su selección >>> '''  # menu para elegir la trigonometría
menuEstad = '''
¿Que función estadística deseas realizar con estos números?
    1) Media
    2) Moda
    3) Mediana
    4) Mínimo
    5) Máximo
    0) Salir
Utilice el número correspondiente a su selección >>> '''  # menu para elegir la estadística
print("Bienvenido a la calculadora")
time.sleep(1)
oper = int()
result = int()
numList = []
maxNum = int(input("Introduce el número de datos a introducir: "))
if maxNum == 0:
    print(Fore.GREEN + "Adios")
    print(Style.RESET_ALL)
    input('Presiona espacio para salir.')
    exit()
while maxNum > len(numList):
    longNumList = str(int(len(numList) + 1))
    numList.append(int(input("Introduce el número " + longNumList + ": ")))
oper = int(input(menuOper))
while True:
    if oper == 1:
        result = sum(numList)
        print(result)
        input('Presiona espacio para salir.')
        break
    elif oper == 2:
        for i in range(len(numList)):
            numList[i] = numList[i] * -1
        numList[0] = numList[0] * -1
        result = sum(numList)
        print(result)
        input('Presiona espacio para salir.')
        break
    elif oper == 3:
        result = functools.reduce(operator.mul, numList)
        print(result)
        input('Presiona espacio para salir.')
        break
    elif oper == 4:
        print('''
            Si has introducido mas de dos datos, 
            ten en cuenta que dividirá el primero entre el segundo, 
            el resultado con el tercero, y asi...''')
        continuar = input("¿Aun asi quieres continuar?'y' para si 'n' para no: ")
        if continuar == "y":
            for i in range(len(numList) - 1):
                numList[0] = numList[0] / numList[i + 1]
            result = numList[0]
            print(result)
            input('Presiona espacio para salir.')
            break
        elif continuar == "n":
            print("Cancelado!")
            input('Presiona espacio para salir.')
            break
    elif oper == 5:
        result = sum(numList)
        result = int(math.sqrt(result))
        print(result)
        input('Presiona espacio para salir.')
        break
    elif oper == 6:
        while True:
            operTrig = int(input(menuTrig))
            if operTrig == 1:
                result = sum(numList)
                result = math.sin(result)
                print(result)
                input('Presiona espacio para salir.')
                break
            elif operTrig == 2:
                result = sum(numList)
                result = math.cos(result)
                print(result)
                input('Presiona espacio para salir.')
                break
            elif operTrig == 3:
                result = sum(numList)
                result = math.tan(result)
                print(result)
                input('Presiona espacio para salir.')
                break
            elif operTrig == 0:
                print(Fore.GREEN + "Adios")
                print(Style.RESET_ALL)
                input('Presiona espacio para salir.')
                exit()
                break
            else:
                print("Debes introducir un número válido")
        break
    elif oper == 7:
        while True:
            operEstad = int(input(menuEstad))
            if operEstad == 1:
                result = sum(numList)
                result = int(result / len(numList))
                print(result)
                break
            elif operEstad == 2:
                result = stat.mode(numList)
                print(result)
                break
            elif operEstad == 3:
                result = stat.median(numList)
                print(result)
                break
            elif operEstad == 4:
                numList.sort()
                result = numList[0]
                print(result)
                input('Presiona espacio para salir.')
                break
            elif operEstad == 5:
                numList.sort()
                result = numList[len(numList)-1]
                print(result)
                input('Presiona espacio para salir.')
                break
            elif operEstad == 0:
                print(Fore.GREEN+"Adios")
                print(Style.RESET_ALL)
                input('Presiona espacio para salir.')
                exit()
            else:
                print("Debes introducir un número disponible.")
        break
    elif oper == 0:
        print(Fore.GREEN+"Adios")
        print(Style.RESET_ALL)
        input('Presiona espacio para salir.')
        exit()
        break
