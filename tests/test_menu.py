from src import menu
from src import data
from unittest.mock import patch


def test_rock_paper_scissors():
    with patch("getpass.getpass", side_effect=["rock", "paper"]):
        assert menu.rock_paper_scissors() == 2
    with patch("getpass.getpass", side_effect=["paper", "rock"]):
        assert menu.rock_paper_scissors() == 1
    with patch("getpass.getpass", side_effect=["scissors", "paper"]):
        assert menu.rock_paper_scissors() == 1
    with patch("getpass.getpass", side_effect=["paper", "scissors"]):
        assert menu.rock_paper_scissors() == 2
    with patch("getpass.getpass", side_effect=["rock", "scissors"]):
        assert menu.rock_paper_scissors() == 1
    with patch("getpass.getpass", side_effect=["scissors", "rock"]):
        assert menu.rock_paper_scissors() == 2


def test_game_menu():
    with patch("builtins.input", side_effect=["1"]):
        assert menu.game_menu() == "1"
    with patch("builtins.input", side_effect=["2"]):
        assert menu.game_menu() == "2"
    with patch("builtins.input", side_effect=["3"]):
        assert menu.game_menu() == "3"
