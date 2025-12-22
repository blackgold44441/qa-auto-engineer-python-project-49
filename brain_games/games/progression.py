import random


RULE_TEXT = 'What number is missing in the progression?'


def generate_progression() -> list:
    start = random.randint(1, 100)
    length = random.randint(5, 10)
    step = random.randint(1, 5)
    progression = []
    for _ in range(length):
        progression.append(start)
        start = start + step
    return progression


def get_round() -> tuple[str, str]:
    current_progression = generate_progression()

    index = random.randint(0, len(current_progression)-1)
    correct_answer = str(current_progression[index])

    current_progression[index] = '..' # Заменили число на точки

    progression_strs = []
    for item in current_progression:
        progression_strs.append(str(item))
        question = ' '.join(progression_strs)
    return question, correct_answer
