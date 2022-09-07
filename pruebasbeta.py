# from unittest import result
# import requests
# import os

# os.system("cls")
# nom=input("Ingrese numero de item: ")
# url="https://pokeapi.co/api/v2/pokemon/"+nom
# data=requests.get(url)

# if data.status_code == 200:
#     data=data.json()
#     nombre=data.get("abilities")
#     habilidad=nombre.get("ability")
#     nom_hab=habilidad.get("name")
    
#     os.system("cls")
#     print(f"""
#     ===========================
#     Habilidad:{nom_hab}
    
#     ===========================
#     """)


# if results:
#     for pokemon in results:
#         name=pokemon["name"]
#         print(name)
