from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

# Define route for handling POST requests
@app.route('/', methods=['POST'])
def handle_post():
    # Run stress_cpu.py script in a separate process
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return jsonify({"message": "CPU stress initiated"}), 200

# Define route for handling GET requests
@app.route('/', methods=['GET'])
def get_private_ip():
    # Get private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app on port 5000
