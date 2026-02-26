import random

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

def agent(observation, configuration=None):
    """
    observation example:
    {
        "position": [x, y],
        "resources": [[x1,y1],[x2,y2]]
    }
    """

    pos = observation["position"]
    resources = observation.get("resources", [])

    # move toward nearest resource
    if resources:
        target = min(resources, key=lambda r: abs(r[0]-pos[0]) + abs(r[1]-pos[1]))
        dx = target[0] - pos[0]
        dy = target[1] - pos[1]

        if abs(dx) > abs(dy):
            return "RIGHT" if dx > 0 else "LEFT"
        else:
            return "DOWN" if dy > 0 else "UP"

    return random.choice(ACTIONS)
