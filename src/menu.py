import getpass
from src import data


def rock_paper_scissors():
    winner = 0
    player_1 = ""
    player_2 = ""
    tie = 0
    data.stats["Games"] += 1
    print("\n" + "=" * 35)
    print("    WELCOME TO ROCK PAPER SCISSORS!")
    print("=" * 35)
    print("Beat your opponent to earn the right to choose a quiz topic!")
    print()
    while True:
        while True:
            player_1 = (
                getpass.getpass("Player 1, choose Rock, Paper, or Scissors: ")
                .strip()
                .upper()
            )
            if player_1 not in ["ROCK", "PAPER", "SCISSORS"]:
                print("Invalid Input")
                continue
            else:
                break
        while True:
            player_2 = (
                getpass.getpass("Player 2, choose Rock, Paper, or Scissors: ")
                .strip()
                .upper()
            )
            if player_2 not in ["ROCK", "PAPER", "SCISSORS"]:
                print("Invalid Input")
                continue
            else:
                break
        if player_1 == player_2:
            tie += 1
            data.stats["Ties"] += 1
            if tie >= 4:
                print("STOP TYING")
            print("Tie Game Go Again")

            continue
        if player_1 == "ROCK" and player_2 == "SCISSORS":
            winner = 1
            data.stats["Player 1W"] += 1
            data.stats["Player 2L"] += 1
        elif player_2 == "ROCK" and player_1 == "SCISSORS":
            winner = 2
            data.stats["Player 2W"] += 1
            data.stats["Player 1L"] += 1
        elif player_2 == "PAPER" and player_1 == "SCISSORS":
            winner = 1
            data.stats["Player 1W"] += 1
            data.stats["Player 2L"] += 1
        elif player_1 == "PAPER" and player_2 == "SCISSORS":
            winner = 2
            data.stats["Player 2W"] += 1
            data.stats["Player 1L"] += 1
        elif player_2 == "PAPER" and player_1 == "ROCK":
            winner = 2
            data.stats["Player 2W"] += 1
            data.stats["Player 1L"] += 1
        elif player_1 == "PAPER" and player_2 == "ROCK":
            winner = 1
            data.stats["Player 1W"] += 1
            data.stats["Player 2L"] += 1
        break
    print(f"Player 1 chose: {player_1}")
    print(f"Player 2 chose: {player_2}")
    if winner == 2:
        print(f"{player_2} beats {player_1}!")
    if winner == 1:
        print(f"{player_1} beats {player_2}!")

    return winner


def game_menu():
    if data.stats["Games"] > 0:
        win_rate_1 = (data.stats["Player 1W"] / data.stats["Games"]) * 100
        win_rate_2 = (data.stats["Player 2W"] / data.stats["Games"]) * 100
    else:
        win_rate_1 = 0
        win_rate_2 = 0
    choice = input("Choose an Action (Enter 1-3):").strip()
    if choice not in "123":
        print("Invalid Choice Enter An Accepted Value")
        return game_menu()

    if choice == "1":
        return choice
    elif choice == "2":
        print("\nCURRENT STATISTICS")
        print(f"Games Won By Player 1: {data.stats['Player 1W']}")
        print(f"Games Won By Player 2: {data.stats['Player 2W']}")
        print(f"Games Lost By Player 1: {data.stats['Player 1L']}")
        print(f"Games Lost By Player 2: {data.stats['Player 2L']}")
        print(f"Games Tied: {data.stats['Ties']}")
        print(f"Total Games: {data.stats['Games']}")
        print(f"Player 1 Win Rate: {win_rate_1}%")
        print(f"Player 2 Win Rate: {win_rate_2}%")
        return choice
    elif choice == "3":
        print("\n" + "=" * 40)
        print("         FINAL GAME STATISTICS")
        print("=" * 40)

        print(f"Total Games: {data.stats['Games']}")
        print(f"Player 1 Wins: {data.stats['Player 1W']}")
        print(f"Player 2 Wins: {data.stats['Player 2W']}")
        print(f"Ties: {data.stats['Ties']}")

        print(f"Player 1 Win Rate: {win_rate_1:.2f}%")
        print(f"Player 2 Win Rate: {win_rate_2:.2f}%")

        print("\nThanks for playing Rock Paper Scissors!")
        print("=" * 40)
        return choice


def quiz_game():
    player = rock_paper_scissors()
    pass
