from imagenesascii import *
import os
from pokemonBD import *

class Pokemon:
    def __init__(self,nombre,color,tipo,fuerza,defensa,vida,img,index):
        self.nombre=nombre
        self.color=color
        self.tipo=tipo
        self.fuerza=fuerza
        self.defensa=defensa
        self.vida=vida
        self.img=pokeimg[img]
        self.index=index
    
    def pokedex(self):
        print(f"""
        ========POKEDEX==========================       
        Nombre:{self.nombre}    Fuerza:{self.fuerza}
        Color:{self.color}      Defensa:{self.defensa}
        Tipo:{self.tipo}        Vida:{self.vida}
        =========================================
        {self.img}
        """)


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