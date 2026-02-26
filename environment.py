import random

GRID_SIZE = 7
MAX_TURNS = 200

def random_pos():
    return [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]

def get_initial_state():
    return {
        "turn": 0,
        "agents": {
            i: {"pos": random_pos(), "score": 0}
            for i in range(4)
        },
        "resources": [random_pos() for _ in range(10)]
    }

def move(pos, action):
    x, y = pos
    if action == "UP": y -= 1
    elif action == "DOWN": y += 1
    elif action == "LEFT": x -= 1
    elif action == "RIGHT": x += 1

    x = max(0, min(GRID_SIZE-1, x))
    y = max(0, min(GRID_SIZE-1, y))
    return [x, y]

def step(state, actions):
    for i, action in actions.items():
        state["agents"][i]["pos"] = move(state["agents"][i]["pos"], action)

        if state["agents"][i]["pos"] in state["resources"]:
            state["agents"][i]["score"] += 1
            state["resources"].remove(state["agents"][i]["pos"])

    state["turn"] += 1
    return state
