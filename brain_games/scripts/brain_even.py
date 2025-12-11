import random
from prompt import string


RULE_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
ROUNDS_COUNT = 3


def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(RULE_TEXT)

    for _ in range(ROUNDS_COUNT):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = string("Your answer: ")

        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()