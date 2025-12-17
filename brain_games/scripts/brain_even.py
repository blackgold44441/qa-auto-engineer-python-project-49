import random
from brain_games.engine import run_game


RULE_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round() -> tuple[str, str]:
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def main() -> None:
    run_game(RULE_TEXT, get_round)


if __name__ == "__main__":
    main()