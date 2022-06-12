from click import option
import time
import os
import sys

#Introductor
n1 = int(input("Ingrese Primer Dígito: "))
n2 = int(input("Ingrese Segundo Dígito: "))
#Seleccionador
while True:
    print("""
    1)Sumar
    2)Restar
    3)Multipicar
    4)Dividir
    5)Cambiar los Digitos
    6)Cerrar
    """)
    Sumar = "1" 
    Restar = "2"
    Multipicar = "3"
    Dividir = "4"
    ChooseDigit = "5"
    Cerrar = "6"

    Selector = input("Seleccione un Número del 1-6: ")
#Operaciones y Decisiones
    if Selector == Sumar : 
        print("Resultado:",n1,"+",n2,"=",n1+n2)
        time.sleep(5)
    if Selector == Restar :
        print("Resultado:",n1,"-",n2,"=",n1-n2)
        time.sleep(5)
    if Selector == Multipicar :
        print("Resultado:",n1,"*",n2,"=",n1*n2)
        time.sleep(5)
    if Selector == Dividir :
        print("Resultado:",n1,":",n2,"=",n1/n2)
        time.sleep(5)
    if Selector == ChooseDigit :
        n1 = int(input("Ingrese Primer Dígito: "))
        n2 = int(input("Ingrese Segundo Dígito: "))
    if Selector == Cerrar :
        sys.exit("Cerrando...")