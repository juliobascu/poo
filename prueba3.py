# import pywhatkit

# # Envía un mensaje a las 11:30 AM debe ser formato 24hs
# hora=14
# minuto=14
# mensaje="Conectense a discord po"
# numero="+56963573518"
# nombre="Julio"
# lista=["+56963573518","+56979034670","+56958799275","+56988659715"]
# for i in lista:
#     pywhatkit.sendwhatmsg(i,mensaje,hora,minuto)
#     minuto=minuto+1
#---------------------------------------------------------------------------
# import speech_recognition as sr

# # Obtén una muestra de audio del micrófono
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     audio = r.listen(source)

# # Convierte el audio en texto
# text = r.recognize_google(audio)
# print(text)
#-----------------------------------------------------------------------------
# import cv2

# # Abrir la cámara del computador
# camera = cv2.VideoCapture(0)

# # Continuar mostrando la vista en vivo de la cámara hasta que se presione 'q'
# while True:
#     # Leer un frame de la cámara
#     _, frame = camera.read()

#     # Mostrar el frame en una ventana
#     cv2.imshow("Live Camera", frame)

#     # Si se presiona 'q', detener el bucle
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Liberar la cámara y destruir la ventana
# camera.release()
# cv2.destroyAllWindows()
#------------------------------------------------------------------------------------------------
# import requests
# peticionuser={"api_dev_key":"3ega9lJK0q51mdpQO7icVSIJftIHtY4q","api_user_name":"juliobascu","api_user_password":"Isabellabascu1409"}        
# userkey=requests.post("https://pastebin.com/api/api_login.php",data=peticionuser)
# print(userkey.text)
#-----------------------------------------------------------------------------------------------

from flask import Flask, request,jsonify
from logs_bd import log_pokemon


app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/logs')
def ver_logs():
    return jsonify(log_pokemon)

@app.route('/logs',methods=['POST'])
def agregar_log():
    new_log={
        "nombre":request.json["nombre"],
        "tipo":request.json["tipo"],
        "peso":request.json["peso"],
        "altura":request.json["altura"],
        "pokeid":request.json["pokeid"],
        "hp":request.json["hp"],
        "atk":request.json["atk"],
        "def":request.json["def"],
        "sprite":request.json["sprite"]
    }
    log_pokemon.append(new_log)
    return jsonify({"favoritos":log_pokemon})

if __name__ == '__main__':
    app.run()

# @app.route('/', methods=['PUT'])
# def update_user():
#     data = request.json
#     name = data['name']
#     return f"Usuario {name} actualizado"

# @app.route('/', methods=['DELETE'])
# def delete_user():
#     name = request.args.get('name')
#     return f"Usuario {name} eliminado"



