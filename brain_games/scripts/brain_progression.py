from brain_games.engine import run_game
from brain_games.games.progression import RULE_TEXT, get_round


def main() -> None:
    run_game(RULE_TEXT, get_round)


if __name__ == "__main__":
    main()