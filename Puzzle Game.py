import random

def start_game():
    print("🔐 Welcome to the Escape Room!")
    print("Solve puzzles to escape. Type 'exit' anytime after a round to quit.\n")

    while True:
        score = 0
        puzzles = [
            ("What 5-letter word becomes shorter when you add 2 letters to it?", "short"),
            ("I’m tall when I’m young, and short when I’m old. What am I?", "candle"),
            ("a=z, b=y, c=x, ..., z=a. Decode 'zivgrm'", "artist")
        ]

        random.shuffle(puzzles)

        for i, (question, correct_answer) in enumerate(puzzles):
            score = run_puzzle(i + 1, question, correct_answer, score)

        print(f"\n🏁 Your final score: {score}/3")
        save_score(score)

        choice = input("\nType 'exit' to quit or press Enter to play again: ").lower().strip()
        if choice == 'exit':
            print("👋 Thanks for playing. Goodbye!")
            break
        print("\n🔄 Starting a new game...\n")

def run_puzzle(number, question, correct_answer, score):
    attempts = 3
    while attempts > 0:
        print(f"🧩 Puzzle {number}: {question}")
        answer = input("Your answer: ").lower()
        if answer == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
            break
        else:
            attempts -= 1
            score = max(0, score - 1)
            print(f"❌ Wrong. Attempts left: {attempts} | Score: {score}\n")
    if attempts == 0:
        print("🚪 Moving to next puzzle...\n")
    return score

def save_score(score):
    name = input("Enter your name to save your score: ")
    try:
        with open("score_log.txt", "a") as file:
            file.write(f"{name}: {score}/3\n")
        print("✅ Score saved to 'score_log.txt'.")
    except:
        print("⚠️ Could not save score.")

if __name__ == '__main__':
    start_game()
