from src import menu
from src.main import run_game
from unittest.mock import patch


def test_run_game():

    with patch("builtins.input", return_value="1"):
        with patch("src.menu.getpass.getpass", side_effect=["rock", "paper"]):
            assert run_game() == 2
        with patch("src.menu.getpass.getpass", side_effect=["paper", "rock"]):
            assert run_game() == 1
