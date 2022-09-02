from imagenesascii import *
class Pokemon:
    def __init__(self,nombre,color,tipo,fuerza,defensa,vida,img):
        self.nombre=nombre
        self.color=color
        self.tipo=tipo
        self.fuerza=fuerza
        self.defensa=defensa
        self.vida=vida
        self.img=pokeimg[img]
    
    def pokedex(self):
        print(f"""
        ========POKEDEX==========================       
        Nombre:{self.nombre}    Fuerza:{self.fuerza}
        Color:{self.color}      Defensa:{self.defensa}
        Tipo:{self.tipo}        Vida:{self.vida}
        =========================================
        {self.img}
        """)