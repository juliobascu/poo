from flask import Flask, request,jsonify
from logs_bd import logpokemon


app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/logs')
def ver_logs():
    return jsonify(logpokemon)

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
    logpokemon.append(new_log)
    return jsonify({"favoritos":logpokemon})



@app.route('/logs/<string:logpokemon_nombre>', methods=['PUT'])
def editar_log(logpokemon_nombre):
    pokemonEncontrado=[i for i in logpokemon if i["nombre"]==logpokemon_nombre]
    if (len(pokemonEncontrado)) > 0:
        pokemonEncontrado[0]["nombre"] = request.json["nombre"]

        return jsonify({"log_pokemon":pokemonEncontrado[0]})
    return jsonify({"mensaje":pokemonEncontrado}) 


@app.route('/logs/<string:logpokemon_nombre>', methods=['DELETE'])
def borrar_log(logpokemon_nombre):
    pokemonEncontrado=[i for i in logpokemon if i["nombre"]==logpokemon_nombre]
    if (len(pokemonEncontrado)) > 0:
        logpokemon.remove(pokemonEncontrado[0])
        return jsonify({
            "mensaje":"Pokemon borrado de la lista de favoritos",
            "pokemones":logpokemon
            }) 
    return jsonify({"mensaje":"pokemon no encontrado!"})

if __name__ == '__main__':
    app.run()

