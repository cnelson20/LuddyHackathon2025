class TrafficLightAgent:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.state = 'red'

    def update(self, emv_position):
        if abs(self.position[0] - emv_position[0]) + abs(self.position[1] - emv_position[1]) <= 1:
            self.state = 'green'
        else:
            self.state = 'red'

    def serialize(self):
        return {'name': self.name, 'position': self.position, 'state': self.state}


class EMVAgent:
    def __init__(self, name, start, goal):
        self.name = name
        self.position = start
        self.goal = goal
        self.path = self.generate_path()

    def generate_path(self):
        # Straight-line path for MVP
        path = []
        x, y = self.position
        gx, gy = self.goal
        while x != gx:
            x += 1 if gx > x else -1
            path.append((x, y))
        while y != gy:
            y += 1 if gy > y else -1
            path.append((x, y))
        return path

    def update(self, grid, lights):
        if self.path:
            next_pos = self.path[0]
            for light in lights:
                if light.position == next_pos and light.state == 'green':
                    self.position = self.path.pop(0)
                    break

    def serialize(self):
        return {'name': self.name, 'position': self.position}