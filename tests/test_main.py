from src import menu, main
from src.main import run_game
from unittest.mock import patch


def test_run_game():
    with (
        patch.object(main.menu, "game_menu", side_effect=["1", "2", "3", "4"]),
        patch.object(main.menu, "quiz_game") as quiz,
        patch.object(main.menu, "view_high_scores") as scores,
        patch.object(main.menu, "rock_game_menu", side_effect=["1", "2", "3"]),
        patch.object(main.menu, "rock_paper_scissors") as rps,
    ):
        main.run_game()

        quiz.assert_called_once()
        scores.assert_called_once()
        rps.assert_called_once()
