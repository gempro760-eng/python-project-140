import random

import prompt

ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_DIVISOR = 2
SQUARE_ROOT_RANGE_OFFSET = 1


def is_prime(number):
    if number < MIN_DIVISOR:
        return False
    for i in range(
        MIN_DIVISOR,
        int(number**0.5) + SQUARE_ROOT_RANGE_OFFSET,
    ):
        if number % i == 0:
            return False
    return True


def play_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(ROUNDS_COUNT):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = "yes" if is_prime(number) else "no"

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