from brain_games.games.gcd import RULE_TEXT, get_round
from brain_games.engine import run_game


def main() -> None:
    run_game(RULE_TEXT, get_round)


if __name__ == "__main__":
    main()