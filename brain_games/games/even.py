import random

import prompt

ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100
EVEN_DIVISOR = 2


def is_even(number):
    return number % EVEN_DIVISOR == 0


def play_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS_COUNT):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = "yes" if is_even(number) else "no"

        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        if user_answer.strip().lower() == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")