import random

RULE_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True
                

def get_round() -> tuple[str, str]:
    number = random.randint(1, 100)
    question = f'{number}'
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer