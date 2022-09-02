class Pokemon:
    def __init__(self,nombre,color,tipo,fuerza,defensa,vida):
        self.nombre=nombre
        self.color=color
        self.tipo=tipo
        self.fuerza=fuerza
        self.defensa=defensa
        self.vida=vida
    
    def pokedex(self):
        print(f"""
        ========POKEDEX==========================       
        Nombre:{self.nombre}    Fuerza:{self.fuerza}
        Color:{self.color}      Defensa:{self.defensa}
        Tipo:{self.tipo}        Vida:{self.vida}
        =========================================

        """)
    
pokemon01=Pokemon("Pikachu","Amarillo","Electrico",50,30,100)
pokemon01.pokedex()