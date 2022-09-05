from pokemonBD import *

archivo=open("pokemon.txt","w")
archivo.write("Nombre:%s "%listapokedex[0].nombre+"\n")
archivo.write("Color: %s"%listapokedex[0].color+"\n")
archivo.write("Tipo: %s"%listapokedex[0].tipo+"\n")
archivo.write("Fuerza: %s"%listapokedex[0].fuerza+"\n")
archivo.write("Defensa: %s"%listapokedex[0].defensa+"\n")
archivo.write("Vida: %s"%listapokedex[0].vida+"\n")



# archivo.write(print(f"""
#         ========POKEDEX==========================       
#         Nombre:{listapokedex[0].nombre}    Fuerza:{listapokedex[0].fuerza}
#         Color:{listapokedex[0].color}      Defensa:{listapokedex[0].defensa}
#         Tipo:{listapokedex[0].tipo}        Vida:{listapokedex[0].vida}
#         =========================================
#         {listapokedex[0].img}
#         """))
