from flask import Flask, render_template
from flask_socketio import SocketIO
from simulation.simulator import start_simulation

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def send_update(state):
    socketio.emit('state_update', state)

start_simulation(socketio, send_update)

if __name__ == '__main__':
    socketio.run(app, debug=True)