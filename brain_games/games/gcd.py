import random

RULE_TEXT = 'Find the greatest common divisor of given numbers.'


def gcd(num1: int, num2: int) -> int:
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def get_round() -> tuple[str, str]:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer