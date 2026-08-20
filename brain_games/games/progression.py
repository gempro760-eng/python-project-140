import random

import prompt

ROUNDS_COUNT = 3
START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 10
LENGTH_MIN = 5
LENGTH_MAX = 10
FIRST_INDEX = 0
INDEX_OFFSET = 1


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def play_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(ROUNDS_COUNT):
        start = random.randint(START_MIN, START_MAX)
        step = random.randint(STEP_MIN, STEP_MAX)
        length = random.randint(LENGTH_MIN, LENGTH_MAX)

        progression = generate_progression(start, step, length)
        hidden_index = random.randint(FIRST_INDEX, length - INDEX_OFFSET)

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