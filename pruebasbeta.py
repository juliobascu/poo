import requests

url="https://pokeapi.co/api/v2/pokemon-form"
data=requests.get(url)

if data.status_code == 200:
    data=data.json()
    results=data.get("results",[])
    
    if results:
        for pokemon in results:
            name=pokemon["name"]
            print(name)