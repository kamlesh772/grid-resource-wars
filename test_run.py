from environment import get_initial_state, step
from starter_agent import agent

state = get_initial_state()

for _ in range(20):
    actions = {}
    for i, data in state["agents"].items():
        observation = {
            "position": data["pos"],
            "resources": state["resources"]
        }
        actions[i] = agent(observation)

    state = step(state, actions)

print("Final Scores:")
for i, data in state["agents"].items():
    print("Agent", i, "Score:", data["score"])
