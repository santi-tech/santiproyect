from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return "¡Hola, Santi! Tu API Flask está funcionando ✅"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre", "amigo")
    return jsonify({"saludo": f"Hola, {nombre}! Esto es Flask en Render 🚀"})

if _name_ == "_main_":
    app.run()
