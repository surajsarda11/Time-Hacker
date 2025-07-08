# main.py
import os
from engine.timeline import Timeline
from engine.parser import CommandParser
from engine.generator import TimelineGenerator


def show_intro():
    intro_path = "assets/intro.txt"
    if os.path.exists(intro_path):
        with open(intro_path) as f:
            print(f.read())


def main():
    print("\n=== TIME HACKER v0.3 ===")
    show_intro()
    print("Type 'help' to see available commands.\n")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    difficulty = input("Select difficulty (easy / medium / hard): ")

    generator = TimelineGenerator(age, difficulty)
    timeline_data = generator.generate()
    timeline = Timeline(timeline_data)
    parser = CommandParser(timeline)

    while not timeline.is_solved():
        cmd = input(f"[{name}@TimeHacker]> ").strip()
        parser.execute(cmd)

    print("\n🎉 YOU HAVE SUCCESSFULLY STABILIZED THE TIMELINE! 🎉")


if __name__ == "__main__":
    main()
