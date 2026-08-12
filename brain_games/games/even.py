import random

import prompt


def is_even(number):
    return number % 2 == 0


def play_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 3

    for _ in range(rounds_count):
        number = random.randint(1, 100)
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