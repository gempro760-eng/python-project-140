import math
import random

import prompt


def play_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds_count = 3

    for _ in range(rounds_count):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

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