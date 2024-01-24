from flask import Flask
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_seed():
    return f"{socket.gethostname()}", 200

@app.route("/", methods=["POST"])
def post_seed():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
