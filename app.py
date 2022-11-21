from flask import Flask, request, jsonify
import json

app=Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/save_json", methods=["GET", "POST"])
def save_json_file():
    data = request.json()
    print(data)
    with open("json_file.json", "w+") as f:
        f.write(json.dumps(data, indent=4))
    return "JSON saved"

@app.route("/get_json", methods=["GET", "POST"])
def get_json_file():
    with open("json_file.json", "w+") as f:
        data = f.readlines()
    data = "\n".join(data) #esto es cadena
    data = json.loads(data) #esto es diccionario
    return jsonify(data)


if __name__ == "__main__":
    app.run()