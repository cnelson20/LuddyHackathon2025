import random

class TrafficLightAgent:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.state = 'red'
        self.role = 'normal'
        self.reward = 0
        self.incoming_queue = random.randint(0, 5)
        self.outgoing_capacity = 5
        self.reward_history = []

    def assign_role(self, emv_position, emv_next_position):
        if self.position == emv_position:
            self.role = 'primary'
        elif self.position == emv_next_position:
            self.role = 'secondary'
        else:
            self.role = 'normal'

    def update_queue(self):
        self.incoming_queue = max(0, self.incoming_queue + random.choice([-1, 0, 1]))

    def traffic_pressure(self):
        return max(0, self.incoming_queue - self.outgoing_capacity)

    def update(self, emv_position, emv_next_position):
        self.assign_role(emv_position, emv_next_position)
        self.update_queue()

        if self.role == "primary":
            self.state = 'green'
            self.reward = -1
        elif self.role == "secondary":
            self.state = 'green' if self.traffic_pressure() < 3 else 'red'
            self.reward = -0.5 * self.traffic_pressure()
        else:
            self.state = 'red'
            self.reward = -self.traffic_pressure()

        self.reward_history.append(self.reward)
        if len(self.reward_history) > 100:
            self.reward_history.pop(0)

    def serialize(self):
        return {
            'name': self.name,
            'position': self.position,
            'state': self.state,
            'role': self.role,
            'reward': self.reward,
            'queue': self.incoming_queue
        }

class EMVAgent:
    def __init__(self, start_position):
        self.position = start_position
        self.path = [(1, 1), (1, 2)]

    def choose_next_step(self, lights):
        return self.path[0] if self.path else self.position

    def update(self, lights):
        if not self.path:
            return
        next_pos = self.path[0]
        light = next((l for l in lights if l.position == next_pos), None)
        if light and light.state == 'green':
            self.position = self.path.pop(0)