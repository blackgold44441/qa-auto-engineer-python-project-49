from prompt import string

ROUNDS_COUNT = 3


def run_game(rule_text: str, get_round):
    # 1) Приветствие и имя
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")

    # 2) Правило игры
    print(rule_text)

    # 3) Раунды
    for _ in range(ROUNDS_COUNT):
        # get_round() должна вернуть:
        # question (строка для вывода) и correct_answer (строка)
        question, correct_answer = get_round()

        print(f"Question: {question}")
        answer = string("Your answer: ")

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    # 4) Победа
    print(f"Congratulations, {name}!")