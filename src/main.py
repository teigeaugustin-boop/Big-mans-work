# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from src import menu


def run_game():
    while True:
        print("\nMENU")
        print("1. Play Round")
        print("2. View Stats")
        print("3. Exit")
        choice = menu.game_menu()
        if choice == "1":
            winner = menu.rock_paper_scissors()
            print(f"\nPLAYER {winner} WINS!")
            print("Congratulations! You've earned the right to pick a quiz topic!")
            print("\nNow choose your quiz topic!")

        if choice == "3":
            break
    return choice


if __name__ == "__main__":
    run_game()
