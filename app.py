from flask import Flask, request, jsonify
import json
import random

app=Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    puntos = []
    # loop para generar carritos internos
    for i in range(10):
        puntos.append({"id": i,
                       "x": random.uniform(0, 10),
                       "y": random.uniform(0, 10),
                       "z": random.uniform(0, 10)})

        # COMO SACAR VALORES RANDOM
        with open("json_file.json", "w+") as f:
            f.write(json.dumps({'cars' : puntos}, indent=4))

    return {'cars': puntos}

# @app.route('/save_json', methods=["GET", "POST"])
# def save_json_file():
#     data = request.json()
#     print(data)
#     with open("json_file.json", "w+") as f:
#         f.write(json.dumps(data, indent=4))
#     return "JSON saved"

# @app.route('/get_json', methods=["GET", "POST"])
# def get_json_file():
#     with open("json_file.json", "w+") as f:
#         data = f.readlines()
#     data = "\n".join(data) #esto es cadena
#     data = json.loads(data) #esto es diccionario
#     return jsonify(data)


if __name__ == "__main__":
    app.run()