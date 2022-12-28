from clases import *
import requests 
from tkinter import *
from turtle import position, width
import cv2
import time
from pygame import mixer
from PIL import ImageTk,Image
ini=0
contlista=Contador_lista(0)

mixer.init()
mixer.music.load("resources/pokesong.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)


#-----------------------------------------------------------------------

def next(pokemon):
    
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    # realizamos la petición a la API
    r = requests.get(url)
    # convertimos los datos recibidos a formato json
    j = r.json()
    # imprimimos los datos
    nombre=j["name"]
    tipo=j["types"][0]["type"]["name"]
    peso=j["weight"]/10
    altura=j["height"]/10
    pokeid=j["id"]
    hp=j["stats"][0]["base_stat"]
    atk=j["stats"][1]["base_stat"]
    defensa=j["stats"][2]["base_stat"]
    Variables.sprite=j["sprites"]["front_default"]
    
#--------------------------------------------------------------------------
    Variables.nombre=j["name"]
    Variables.tipo=j["types"][0]["type"]["name"]
    Variables.peso=j["weight"]/10
    Variables.altura=j["height"]/10
    Variables.pokeid=j["id"]
    Variables.hp=j["stats"][0]["base_stat"]
    Variables.atk=j["stats"][1]["base_stat"]
    Variables.defensa=j["stats"][2]["base_stat"]
#-------------------------------------------------------------------------------------------
    canvas.delete("status")
    archivo=open("pokemon.txt","w")
    archivo.write(f"Nombre:{nombre}\n")
    archivo.write(f"Tipo:{tipo}\n")
    archivo.write(f"Peso:{peso}\n")
    archivo.write(f"Ataque:{atk}\n")
    archivo.write(f"Defensa:{defensa}\n")
    archivo.write(f"Vida:{hp}\n")
    archivo.write(f"Altura:{altura}\n")
    archivo.write(f"ID:{pokeid}\n")
    archivo.close()

    with open("pokemon.txt") as pk:
            leer=pk.read().capitalize()

def labelnombre():#--------------------------numero debajo de la imagen
    canvas.delete("label")
    mensaje=contlista.index    
    canvas.create_text(180,500,text=mensaje,fill="black",font=("times",15,"bold"),tags="label")

def error():
    with open("pokemon0.txt") as pk:
            leer=pk.read().capitalize()
            
    
    canvas.create_text(460,200,text=leer,fill="black",font=("times",20,"bold"),tags="status",anchor=NW)

def videointro():
    #---------------------------------------------------------VIDEO INTRO
    intro=cv2.VideoCapture("resources/intropok.mp4")
    fps=intro.get(cv2.CAP_PROP_FPS)
    delay=1/fps

    while (intro.isOpened()):
        ret, im=intro.read()

        if ret ==False:
            break

        cv2.imshow("imagen",im)

        if cv2.waitKey(1) & 0xFF == 27:
            break
        time.sleep(delay)

    intro.release()
    cv2.destroyAllWindows()
    sonidoentrar=mixer.Sound("resources/enterpokemon.mp3")
    sonidoentrar.play()
    mixer.music.set_volume(0.4)
#videointro()#muestra el video de inicio
#---------------------------------------------------------CREACION DE VENTANA TKINTER
window = Tk()
window.title("Pokedex  by.Julio Bascuñan")
window.geometry("800x600")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.pack()

background_img = PhotoImage(file = f"resources/background1.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)
#-----------------------------------------------------------------
def updateimg():#------------------------------------------------------updatear la imagen
    
    url = Variables.sprite
    r = requests.get(url)
    with open('resources/imgs/00imgtemp.png', 'wb') as f:
        f.write(r.content)

    imagenpkm = Image.open('resources/imgs/00imgtemp.png')
    resize=imagenpkm.resize((150,150),Image.Resampling.LANCZOS)
    nuevimg=ImageTk.PhotoImage(resize)
    image_container=canvas.create_image(180,190, anchor="nw",image=nuevimg)
    canvas.itemconfig(image_container,image="zxc")

    
    
#--------------------------------------------------------------------entry1 buscar
entry1_img = PhotoImage(file = f"resources/img_textBox1.png")
entry1_bg = canvas.create_image(
    532.0, 519.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fb9b05",
    highlightthickness = 0,
    font=("times",15,"bold"))

entry1.place(
    x = 130, y = 490,
    width = 86.0,
    height = 28)

#-------------------------------------------------------------------------------entry 2 editor
entry2_img = PhotoImage(file = f"resources/img_textBox1.png")
entry2_bg = canvas.create_image(
    532.0, 519.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#fb9b05",
    highlightthickness = 0,
    font=("times",15,"bold"))

entry2.place(
    x = 489.0, y = 510,
    width = 86.0,
    height = 28)
#---------------------------------------------------------------Funciones Botones

def b0_click():#boton editar pokemon de lista
    
           
    sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
    sonidoentrar.play()
    contlista.index=contlista.index+1
    buscaredit=entry1.get()
    nombre2=entry2.get()
    url = f"http://localhost:5000/logs/{buscaredit}"
    data = {"nombre": nombre2}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: status code", response.status_code)
    
def b1_click():#boton borrar pokemon de lista
    
        sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
        sonidoentrar.play()
        borrar=entry1.get()
        url = f"http://localhost:5000/logs/{borrar}"

        response = requests.delete(url)

        if response.status_code == 200:
            print(response.json())
        else:
            print("Error: status code", response.status_code)

    
def b5_click():#boton de listar API de pokemones vistos        
        sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
        sonidoentrar.play()
        url = f"http://localhost:5000/logs"

        response = requests.get(url)
        resp=response.json()
        y=200
        for i in resp:
            for key in i:
                if key == "nombre":
                    canvas.create_text(460,y,text=i[key],fill="black",font=("times",12,"bold"),tags="status",anchor=NW)
                    y=y+12
            
        

def b6_click():#boton de añadir a favorito API de pokemones vistos      
        sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
        sonidoentrar.play()
        url = "http://localhost:5000/logs"

        payload = {
                "nombre":Variables.nombre,
                "tipo":Variables.tipo,
                "peso":Variables.peso,
                "altura":Variables.altura,
                "pokeid":Variables.pokeid,
                "hp":Variables.hp,
                "atk":Variables.atk,
                "def":Variables.defensa,
                "sprite":Variables.sprite
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            print(response.text)
        else:
            print(f"Error {response.status_code}: {response.text}")


def b2_click():#--------------Boton Buscar Pokemon
    sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
    sonidoentrar.play()
    buscar=entry1.get()
    labelnombre()
    next(buscar)
    updateimg()    

def b3_click():#volumen arriba Boton
    mixer.music.set_volume(mixer.music.get_volume()+0.1)
    sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
    sonidoentrar.play()

def b4_click():#volumen abajo boton
    mixer.music.set_volume(mixer.music.get_volume()-0.1)
    sonidoentrar=mixer.Sound("resources/pokeboton.mp3")
    sonidoentrar.play()
#-----------------------------------------------------------Imagenes de Botonoes Boton Derecha
img0 = PhotoImage(file = f"resources/edit24.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = b0_click,
    relief = "flat")

b0.place(
    x = 540, y = 456,
    width = 24,
    height = 24)
#----------------------------------------------------------------Boton Izquierda
img1 = PhotoImage(file = f"resources/borrar24.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = b1_click,
    relief = "flat")

b1.place(
    x = 503, y = 456,
    width = 26,
    height = 24)
#-----------------------------------------------------------------Boton Buscar
img2 = PhotoImage(file = f"resources/img_textBox1.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = b2_click,
    relief = "flat",
    text="Buscar",
    background="#FF9B05",
    activebackground="#FF9B05")

b2.place(
    x = 250, y = 520,
    width = 80,
    height = 30)
#---------------------------------------------------------------------------------------------------BOTON LISTAR
img5 = PhotoImage(file = f"resources/listarnuevo64.png")
b0 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = b5_click,
    relief = "flat")

b0.place(
    x = 668, y = 450,
    width = 44,
    height = 44)

#-------------------------------------------------------------boton volumen arriba y abajo
img3 = PhotoImage(file = f"resources/vmas.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = b3_click,
    relief = "flat",
    text="",
    background="#fb6705",
    activebackground="#fb6705")

b3.place(
    x = 207, y = 430,
    width = 40,
    height = 10)

img4 = PhotoImage(file = f"resources/vmenos.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = b4_click,
    relief = "flat",
    text="",
    background="#50f608",
    activebackground="#50f608")

b4.place(
    x = 135, y = 430,
    width = 40,
    height = 10)


img6 = PhotoImage(file = f"resources/añadir32.png")
b4 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = b6_click,
    relief = "flat",
    text="",
    background="#50f608",
    activebackground="#50f608")

b4.place(
    x = 600, y = 455,
    width = 32,
    height = 32)
    
#-----------------------------------------------------------------Texto que muestra el nombre del personaje
msjvol="- VOLUMEN +"
canvas.create_text(190,419,text=msjvol,fill="#545454",font=("times",10,"bold"))
#------------------------------------------------------------------------------------Canvas Muestra editar pokemon
canvas.create_text(535,504,text="Nuevo Nombre",fill="#545454",font=("times",10,"bold"))


#------------------------------------------------------------------------------------Final del programa
window.resizable(False, False)
window.mainloop()
