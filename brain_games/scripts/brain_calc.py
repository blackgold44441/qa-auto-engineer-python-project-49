import random
from prompt import string


RULE_TEXT = 'What is the result of the expression?'
ROUNDS_COUNT = 3
OPERATIONS = ['+', '-', '*']


def calculate_operation(num1: int, num2: int, op: str) -> int:
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case _:
            raise ValueError(f"Unknown operation: {op}")


def main() -> None:
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(RULE_TEXT)

    for _ in range(ROUNDS_COUNT):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(OPERATIONS)
        print(f'Question: {num1} {op} {num2}')
        correct_answer = calculate_operation(num1, num2, op)
        answer = string("Your answer: ")
        try:
            user_answer = int(answer)
        except ValueError:
            user_answer = None
        

        if user_answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
