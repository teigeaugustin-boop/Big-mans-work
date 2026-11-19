import getpass
from src import data
import datetime


def rock_paper_scissors():
    winner = 0
    player_1 = ""
    player_2 = ""
    tie = 0
    data.stats["Games"] += 1
    print("\n" + "=" * 35)
    print("    WELCOME TO THE QUIZ!") if data.quiz else print(
        "    WELCOME TO ROCK PAPER SCISSORS!"
    )
    print("=" * 35)
    print(
        "Beat your opponent to earn the right to choose a quiz topic!"
    ) if data.quiz else ""
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
        print("\nPLAYER 2 WINS!")
    if winner == 1:
        print(f"{player_1} beats {player_2}!")
        print("\nPLAYER 1 WINS!")

    return winner


def rock_game_menu():
    if data.stats["Games"] > 0:
        win_rate_1 = (data.stats["Player 1W"] / data.stats["Games"]) * 100
        win_rate_2 = (data.stats["Player 2W"] / data.stats["Games"]) * 100
    else:
        win_rate_1 = 0
        win_rate_2 = 0
    choice = input("Choose an Action (Enter 1-3):").strip()
    if choice not in "123":
        print("Invalid Choice Enter An Accepted Value")
        return rock_game_menu()

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


def game_menu():
    while True:
        choice = input("Choose an Action (Enter 1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def quiz_game():
    rock_paper_scissors()

    print("Congratulations! You've earned the right to pick a quiz topic!")

    print("\nChoose your quiz topic:")
    print("1. General Knowledge")

    while True:
        topic = input("Enter your choice: ").strip()

        if topic == "1":
            break

        print("Invalid choice. Please select 1.")

    score = 0
    total_questions = len(data.questions)

    print("\n" + "=" * 35)
    print("          STARTING QUIZ")
    print("=" * 35)

    for question_number, question in enumerate(data.questions, start=1):
        print(f"\nQuestion {question_number}: {question['question']}")

        for index, choice in enumerate(question["choices"], start=1):
            print(f"{index}) {choice}")

        while True:
            answer = input("\nEnter your answer (1-4): ").strip()

            if answer in ["1", "2", "3", "4"]:
                break

            print("Invalid answer. Please enter a number from 1-4.")

        if int(answer) - 1 == question["answer_index"]:
            score += 1
            print("Correct! Well done!")
        else:
            correct_answer = question["choices"][question["answer_index"]]
            print(f"Incorrect! The correct answer was {correct_answer}.")

        percentage = round((score / question_number) * 100)
        print(f"Current Score: {score}/{question_number} ({percentage}%)")

    final_percentage = round((score / total_questions) * 100)

    print("\n" + "=" * 35)
    print("          QUIZ COMPLETE!")
    print("=" * 35)
    print(f"Final Score: {score}/{total_questions} ({final_percentage}%)")
    print("Thanks for playing!")

    check_high_score(final_percentage)


def check_high_score(percentage):
    sorted_scores = sorted(
        data.high_scores,
        key=lambda score: score["score"],
        reverse=True,
    )

    if len(sorted_scores) < 5 or percentage >= sorted_scores[4]["score"]:
        print("\nCongratulations! You scored a high score!")

        while True:
            name = input("Enter your name: ").strip()

            if name:
                break

            print("Please enter a name.")

        today = datetime.date.today().strftime("%m/%d/%y")

        data.high_scores.append(
            {
                "name": name,
                "score": percentage,
                "date": today,
            }
        )

        data.high_scores.sort(
            key=lambda score: score["score"],
            reverse=True,
        )

        data.high_scores = data.high_scores[:5]


def view_high_scores():
    print("\n" + "=" * 35)
    print("             HIGH SCORES")
    print("=" * 35)

    if not data.high_scores:
        print("No high scores yet. Complete a quiz to get on the leaderboard!")
        return

    sorted_scores = sorted(
        data.high_scores,
        key=lambda score: score["score"],
        reverse=True,
    )

    for position, score in enumerate(sorted_scores[:5], start=1):
        print(f"{position}. {score['score']}% ({score['name']}) — {score['date']}")
