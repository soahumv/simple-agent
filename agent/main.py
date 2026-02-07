import sys

def run(goal):
    print("Agent started")
    print("Goal:", goal)
    print()

    ideas = [
        "Why overthinking is a survival instinct, not a weakness",
        "The psychology behind why silence makes people uncomfortable",
        "Why your brain prefers familiar pain over unknown happiness"
    ]

    for i, idea in enumerate(ideas, start=1):
        print(f"{i}. {idea}")

    print()
    print("Agent finished")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a goal")
    else:
        run(sys.argv[1])
