import random

import prompt


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def play_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds_count = 3

    for _ in range(rounds_count):
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        length = random.randint(5, 10)

        progression = generate_progression(start, step, length)
        hidden_index = random.randint(0, length - 1)

        correct_answer = str(progression[hidden_index])

        display_progression = [str(x) for x in progression]
        display_progression[hidden_index] = ".."
        question_str = " ".join(display_progression)

        print(f"Question: {question_str}")
        user_answer = prompt.string("Your answer: ")

        if user_answer.strip() == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")