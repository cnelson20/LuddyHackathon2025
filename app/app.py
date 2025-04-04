from flask import Flask, render_template
from flask_socketio import SocketIO
from simulation.agents import TrafficLightAgent, EMVAgent
import time, os

app = Flask(__name__)
socketio = SocketIO(app)

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Initialize agents
traffic_lights = [
    TrafficLightAgent("7th & Woodlawn", (1, 1)),
    TrafficLightAgent("7th & Indiana", (1, 2)),
]
emv = EMVAgent(start_position=(0, 0))

log_list = []

def update_simulation():
    while True:
        emv_next_position = emv.choose_next_step(traffic_lights)
        for light in traffic_lights:
            light.update(emv.position, emv_next_position)
            log_line = (f"[{time.time():.1f}] {light.name}: Role={light.role}, "
                        f"State={light.state}, Queue={light.incoming_queue}, "
                        f"Reward={light.reward:.2f}")
            log_list.append(log_line)

            with open("logs/agent_rewards.csv", "a") as f:
                f.write(f"{time.time()},{light.name},{light.role},{light.reward:.2f}\n")

        emv.update(traffic_lights)
        log_list.append(f"[{time.time():.1f}] EMV moved to {emv.position}")

        state = {
            'emv': emv.position,
            'lights': [light.serialize() for light in traffic_lights],
            'log': log_list[-10:]
        }
        socketio.emit('update', state)
        time.sleep(0.5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(update_simulation)

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)