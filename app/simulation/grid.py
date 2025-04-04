def create_grid():
    intersections = {
        '3rd & Woodlawn': (0, 0),
        '3rd & Indiana':  (1, 0),
        '3rd & Dunn':     (2, 0),
        '7th & Woodlawn': (0, 1),
        '7th & Indiana':  (1, 1),
        '7th & Dunn':     (2, 1),
        '10th & Woodlawn':(0, 2),
        '10th & Indiana': (1, 2),
        '10th & Dunn':    (2, 2),
    }
    lights = [TrafficLightAgent(name, pos) for name, pos in intersections.items()]
    emv = EMVAgent("EMV1", (0, 0), (2, 2))
    return intersections, emv, lights