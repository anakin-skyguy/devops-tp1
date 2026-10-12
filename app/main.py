from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({"application": "DevOps TP1", "status": "running"})


@app.get("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Bonjour {name} !"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)