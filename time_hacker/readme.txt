🕰️ TIME HACKER: Command-Line Time Travel Puzzle Game  
"Rewrite the past. Rethink the future."

🧩 Overview:
Time Hacker is a creative, scenario-driven command-line game where you play as a time-traveling agent tasked with rewriting history to prevent catastrophic futures. Every playthrough is unique, dynamically tailored to your age and chosen difficulty.

🧠 Designed to challenge your logic, ethics, and critical thinking, Time Hacker is not just a game — it’s a time-bending thought experiment.

🎮 How to Play:

1. Run the game:
   python main.py

2. Enter your name, age, and difficulty level (easy / medium / hard).

3. You will receive a mission: a corrupted timeline of events that led to a broken future.

4. Your job is to:
   - Investigate the events
   - Analyze clues
   - Change flawed outcomes
   - Restore stability to the timeline

📜 Core Commands:

| Command                       | Description                                          |
|------------------------------|------------------------------------------------------|
| observe                      | View the timeline and all current events             |
| alter <event_id> <outcome>   | Change an event’s outcome (e.g., `alter e2 Banned`)  |
| log <event_id>               | Read a log or hint related to that event             |
| analyze                      | Get an AI-generated clue (usable once per level)     |
| rewind                       | Undo your last change and regain energy              |
| energy                       | View remaining time energy                           |
| help                         | Show the help menu                                   |
| exit                         | Quit the game                                        |

🎯 Game Objective:

- Stabilize the timeline by correcting 3 major historical events.
- Each correct alteration brings the future closer to stability.
- But be warned — you have limited **time energy**!

✨ Smart Outcome Matching:
You don’t need to guess the exact word. The system understands **synonyms and similar terms** using semantic matching.

Example:
- Correct answer: `Banned`
- Accepted answers: `Prohibited`, `Forbidden`, `Restricted`