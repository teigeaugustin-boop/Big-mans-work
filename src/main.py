# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from src import menu
from src import data


def run_game():
    print("\n" + "=" * 35)
    print("       WELCOME TO THE GAME!")
    print("=" * 35)

    while True:
        print("\nMENU")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Play Rock Paper Scissors")
        print("4. Exit")

        choice = menu.game_menu()

        if choice == "1":
            menu.quiz_game()

        elif choice == "2":
            menu.view_high_scores()

        elif choice == "3":
            while True:
                print("\nMENU")
                print("1. Play Round")
                print("2. View Stats")
                print("3. Exit")

                play = menu.rock_game_menu()

                if play == "1":
                    data.quiz = False
                    menu.rock_paper_scissors()
                elif play == "2":
                    continue
                elif play == "3":
                    break

        elif choice == "4":
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    run_game()
