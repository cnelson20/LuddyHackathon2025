import time
import threading
from .agents import EMVAgent, TrafficLightAgent
from .grid import create_grid

def start_simulation(socketio, send_update):
    _, emv, lights = create_grid()

    def tick():
        while True:
            emv.update(None, lights)
            for light in lights:
                light.update(emv.position)
            state = {
                'emv': emv.serialize(),
                'lights': [light.serialize() for light in lights]
            }
            send_update(state)
            time.sleep(0.5)

    thread = threading.Thread(target=tick)
    thread.daemon = True
    thread.start()