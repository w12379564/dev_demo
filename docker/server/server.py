from flask import Flask, request, jsonify
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

@server.route("/", methods=["POST"])
def echo():
    return jsonify(request.json)
    

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)