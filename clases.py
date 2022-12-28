
import os

#funcion de menu
def menu():
    limpiar()
    print(f"""
    ===============MENU===================
    1.-Lista Pokemon    2.-Buscar Pokemon
    3.-Combate          4.-Salir
    ======================================

    """)

#Funcion para limpiar
def limpiar():
    os.system("cls")

class Contador_lista:
    def __init__(self,index):
        self.index=index
        

class Variables:
    sprite=""
    logleer=""
    nombre=""
    tipo=""
    peso=""
    altura=""
    pokeid=""
    hp=""
    atk=""
    defensa=""
    leer=""