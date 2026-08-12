import random

import prompt


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def play_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    rounds_count = 3
    operations = ["+", "-", "*"]

    for _ in range(rounds_count):
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        operation = random.choice(operations)

        correct_answer = str(calculate(num1, num2, operation))

        print(f"Question: {num1} {operation} {num2}")
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