import math
import random

import prompt

ROUNDS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def play_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(ROUNDS_COUNT):
        num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

        correct_answer = str(math.gcd(num1, num2))

        print(f"Question: {num1} {num2}")
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