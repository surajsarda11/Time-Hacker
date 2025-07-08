# timeline.py
import difflib
from nltk.corpus import wordnet

class Timeline:
    def __init__(self, puzzle_data):
        self.title = puzzle_data["title"]
        self.description = puzzle_data["description"]
        self.events = puzzle_data["events"]
        self.energy = puzzle_data.get("energy", 3)
        self.goal_state = puzzle_data["goal_state"]
        self.history = []  # For rewind
        self.analyze_used = False

    def display(self):
        print(f"\n--- {self.title} ---")
        print(self.description)
        for e in self.events:
            print(f"[{e['id']}] {e['description']} → {e['outcome']}")
        print(f"\n⏳ Energy remaining: {self.energy}")

    def alter(self, event_id, new_outcome):
        event = next((e for e in self.events if e["id"] == event_id.lower()), None)
        if not event:
            print("❌ Event not found.")
            return

        if self.energy <= 0:
            print("⚠️ No energy left to alter the timeline!")
            return

        correct = self.goal_state.get(event_id.lower())
        if not correct:
            print("⚠️ No correct outcome available for this event.")
            return

        new_clean = new_outcome.strip().lower()
        correct_clean = correct.strip().lower()

        # Check exact or fuzzy match
        close = difflib.get_close_matches(new_clean, [correct_clean], n=1, cutoff=0.8)

        # Check for synonym match (word-by-word)
        def synonyms(word):
            syns = wordnet.synsets(word)
            return set(lemma.name().lower().replace('_', ' ') for s in syns for lemma in s.lemmas())

        def is_synonym_match(new_phrase, correct_phrase):
            new_words = set(new_phrase.split())
            correct_words = set(correct_phrase.split())
            for word in correct_words:
                all_syns = synonyms(word)
                if not (word in new_words or new_words.intersection(all_syns)):
                    return False
            return True

        if new_clean == correct_clean or close or is_synonym_match(new_clean, correct_clean):
            print("✅ Event stabilized.")
            event["outcome"] = correct  # Normalize to correct answer
        else:
            print("❌ That outcome doesn't fix the event.")
            self.energy -= 1
            return

        self.history.append((event_id, event["outcome"]))
        if self.is_solved():
            print("\n✅ TIMELINE STABILIZED — THE FUTURE IS SAFE!")
            print("🎉 YOU HAVE SUCCESSFULLY STABILIZED THE TIMELINE! 🎉")

    def is_solved(self):
        current_state = {e['id']: e['outcome'] for e in self.events}
        return current_state == self.goal_state

    def rewind(self):
        if not self.history:
            print("🔁 No previous actions to rewind.")
            return
        event_id, old_outcome = self.history.pop()
        for e in self.events:
            if e['id'] == event_id:
                e['outcome'] = old_outcome
                self.energy += 1
                print(f"↩️ Reverted event {event_id} to '{old_outcome}' (energy refunded)")
                return

    def log(self, event_id):
        for e in self.events:
            if e['id'] == event_id:
                if 'log' in e:
                    print(f"\n📜 LOG {event_id.upper()}:\n{e['log']}")
                else:
                    print(f"⚠️ No log available for event {event_id}")
                return
        print(f"❌ Event {event_id} not found.")

    def analyze(self):
        if self.analyze_used:
            print("🧠 Analyze already used in this level.")
            return
        self.analyze_used = True
        hints = []
        for e in self.events:
            correct = self.goal_state.get(e['id'], "")
            if e['outcome'].strip().lower() != correct.strip().lower():
                keyword = correct.split()[0]
                hints.append(f"- Event {e['id']} might need to start with \"{keyword}\".")
        if hints:
            print("🧠 AI HINTS:")
            for h in hints:
                print(h)
        else:
            print("✅ All events seem aligned already!")
