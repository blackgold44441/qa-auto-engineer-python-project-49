import random

RULE_TEXT = 'What is the result of the expression?'
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


def get_round() -> tuple[str, str]:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(OPERATIONS)
    question = f'{num1} {op} {num2}'
    correct_answer = str(calculate_operation(num1, num2, op))
    return question, correct_answer