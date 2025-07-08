# engine/generator.py
import random

class TimelineGenerator:
    def __init__(self, age, difficulty):
        self.age = age
        self.difficulty = difficulty.lower()
        self.event_count = 3 if difficulty == "easy" else 4 if difficulty == "medium" else 5

    def generate(self):
        technologies = ["AI weapons", "climate drones", "bio-labs", "autonomous war bots", "energy reactors"]
        sectors = ["global trade", "water supply", "tech ethics", "forest policy", "data regulation"]
        years = list(range(2030, 2150))

        events = []
        goal_state = {}
        outcomes_easy = ["Ignored", "Failed", "Unregulated"]
        outcomes_hard = ["Banned", "Deployed", "Enforced strictly"]

        for i in range(self.event_count):
            year = random.choice(years)
            tech = random.choice(technologies)
            sector = random.choice(sectors)

            desc = f"{tech} impact on {sector} in {year}"
            wrong = random.choice(outcomes_easy)
            correct = random.choice(outcomes_hard)

            event = {
                "id": f"e{i+1}",
                "description": desc,
                "outcome": wrong,
                "log": f"{tech} created problems in {sector}. It should have been {correct.lower()}."
            }

            events.append(event)
            goal_state[event["id"]] = correct

        return {
            "title": "Generated Timeline: Save the Future",
            "description": f"A custom timeline generated for age {self.age} on {self.difficulty} difficulty.",
            "energy": self.event_count,
            "events": events,
            "goal_state": goal_state
        }
