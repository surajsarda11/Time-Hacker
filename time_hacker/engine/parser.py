import nltk
import difflib
from nltk.corpus import wordnet

nltk.download('wordnet')

class CommandParser:
    def __init__(self, timeline):
        self.timeline = timeline

    def execute(self, cmd):
        parts = cmd.split()
        if not parts:
            return

        action = parts[0].lower()

        if action == "help":
            self.help()
        elif action == "observe":
            self.timeline.display()
        elif action == "alter":
            if len(parts) < 3:
                print("Usage: alter <event_id> <new_outcome>")
                return
            event_id = parts[1]
            new_outcome = " ".join(parts[2:])

            # 🛡️ Anti-mistype safety: detect accidental repeated command
            if "alter" in new_outcome.lower():
                print("⚠️ Oops! It looks like you accidentally typed 'alter' in the outcome. Please try again.")
                return

            # 🔍 Fuzzy and synonym-based matching built into timeline.alter()
            self.timeline.alter(event_id, new_outcome)
        elif action == "rewind":
            self.timeline.rewind()
        elif action == "log":
            if len(parts) != 2:
                print("Usage: log <event_id>")
                return
            self.timeline.log(parts[1])
        elif action == "analyze":
            self.timeline.analyze()
        elif action == "energy":
            print(f"🔋 Energy left: {self.timeline.energy}")
        elif action == "exit":
            exit()
        else:
            print("Unknown command. Type 'help'.")

    def help(self):
        print("""
Available commands:
  observe                - View current timeline and events
  alter <id> <outcome>   - Change outcome of a historical event
  rewind                 - Undo your last alteration
  log <id>               - View detailed log or hint for an event
  analyze                - Get limited-use AI-generated hint
  energy                 - Check remaining time energy
  help                   - Show this help message
  exit                   - Quit the game
""")
