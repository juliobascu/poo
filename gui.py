from cProfile import label
from ctypes.wintypes import RGB
from tkinter import *
import tkinter
import cv2
from imagenesascii import *
from clases import *
import time
from pygame import mixer

mixer.init()
mixer.music.load("resources/pokesong.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)


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
#---------------------------------------------------------

def btn_clicked():
    print("Button Clicked")


window = Tk()

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

background_img = PhotoImage(file = f"resources/background.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)

canvas.create_text(
    335, 40.5,
    text = "Hecho por Julio Bascuñan",
    fill = "#ffffff",
    font = ("Inter-ExtraBold", int(12.0)))

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
    x = 489.0, y = 504,
    width = 86.0,
    height = 28)

img0 = PhotoImage(file = f"resources/RightButton.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 540, y = 456,
    width = 24,
    height = 24)

img1 = PhotoImage(file = f"resources/LeftButton.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 503, y = 456,
    width = 26,
    height = 24)

#-------------------------------------------------------
mensaje="PIKACHU"
canvas.create_text(180,500,text=mensaje,fill="black",font=("times",15,"bold"))
window.resizable(False, False)
window.mainloop()
