import openai
from skimage import io
import os

# Establecemos la API Key
openai.api_key = "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"

def imagen():
    #ingresamos un prompt
    os.system("cls")
    op=input("Ingrese que imagen desea crear y sea muy especifico: ")
    # Generamos una imagen con la API
    response = openai.Image.create(prompt=op, n=1,size="512x512")
    image_url = response['data'][0]['url']
    # Mostramos la imagen
    image = io.imread(image_url)
    io.imshow(image)
    io.show()

def completar():
    #completa lo que le pides con la API
    op=input("Ingresa tu pregunta o una orden: ")
    respuesta=openai.Completion.create(
    model="text-davinci-003",
    prompt=op,
    max_tokens=1500,
    temperature=0
    )
    print(respuesta["choices"][0]["text"])
    input()
def menu():
    os.system("cls")
    print("""
    ===================MENU=======================
    1.-Generar Imagen       2.-Completar Texto
    3.-Salir
    ==============================================
    """)

while True:
    menu()
    op=input("Ingrese seleccion: ")
    if op == "1":
        imagen()
    elif op == "2":
        completar()
    elif op == "3":
        os._exit()

