#importamos módulos necesarios
import requests 
import json 
import os
from skimage import io

ts=1
privatekey="7dea482c6bd1f3ccdf618e4aa420f44628d6e61b"
publickey="903eb20e5c4b70d46e6b782f43d278ce"
#17dea482c6bd1f3ccdf618e4aa420f44628d6e61b903eb20e5c4b70d46e6b782f43d278ce
hashkey="3acc50af3b206a6aa55b54b501f1e924"
os.system("cls")
op=input("Ingrese nombre del personaje a buscar:")

url=f"http://gateway.marvel.com/v1/public/characters?name={op}&ts=1&apikey=903eb20e5c4b70d46e6b782f43d278ce&hash=3acc50af3b206a6aa55b54b501f1e924"

r=requests.get(url)
print(r)
j=json.loads(r.text)

nombre=j["data"]['results'][0]["name"]
#--------------------------------------------------------------------------------------------------
descripcion=j["data"]["results"][0]["description"]
#--------------------------------------------------------------------------traducir con google
# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# payload = f"q={descripcion}&target=es&source=en"
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "208c24c1eemsh70c0307617fcb35p1e3a7djsneddb7e91a187",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

# response = requests.request("POST", url, data=payload, headers=headers)
# rtxt=response.text
# total=rtxt[0]
# print(rtxt)
#------------------------------------------------------------------------------------------------

fotopath=j["data"]["results"][0]["thumbnail"]["path"]
fotoexten=j["data"]["results"][0]["thumbnail"]["extension"]
imagen=fotopath+"."+fotoexten

os.system("cls")
print(nombre)
print(descripcion)

print(f"""
==============================================
1.-Ver Imagen de {op}   2.-SALIR
==============================================
""")
opc=input("selecione una opcion: ")
if opc == "1":
    image = io.imread(imagen)
    io.imshow(image)
    io.show()
elif opc == "2":
    os._exit()




