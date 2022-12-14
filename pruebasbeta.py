#importamos módulos necesarios
import requests 
import json 
import os

#creamos nuestro menu principal
def menu():
    os.system("cls")
    print('Bienvenido al programa para acceder a la API')
    print('Seleccione una opción:')
    print('1. Obtener datos de un Pokemon')
    print('2. Salir del programa')
    opcion = int(input('Opción: '))
    return opcion

# creamos una función para obtener los datos de la API
def getData(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    # realizamos la petición a la API
    r = requests.get(url)
    # convertimos los datos recibidos a formato json
    j = r.json()
    # imprimimos los datos
    nombre=j["name"]
    tipo=j["types"]
    peso=j["weight"]
    altura=j["height"]
    pokeid=j["id"]
    hp=j["stats"][0]["base_stat"]
    atk=j["stats"][1]["base_stat"]
    defensa=j["stats"][2]["base_stat"]
    print(f"""
    ===================================================
    Nombre:{nombre}  Tipo: {tipo[0]["type"]["name"]}
    Peso: {peso/10}kg    Altura:{altura/10} mts     ID:{pokeid}
    HP:{hp}     ATAQUE:{atk}    DEFENSA:{defensa}
    ===================================================
    """)
    input()

# creamos nuestro bucle principal
while True:
    # llamamos a nuestra función de menú
    opcion = menu()
    # comprobamos la opción seleccionada
    if opcion == 1: # obtener datos
        op=input("Ingrese el nombre del pokemon a buscar: ")
        getData(op)

    elif opcion == 2: # salir
        break
    else:
        print('Opción no válida.')