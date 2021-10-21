import pyinputplus as pyip
import random
import time


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def answer(operator, num1, num2):
    if operator == "*":
        return multiplication(num1, num2)
    elif operator == "+":
        return addition(num1, num2)
    elif operator == "-":
        return subtraction(num1, num2)


def continue_game():
    print("Continue playing? (y/n)")
    option = input("Enter your choice: ")
    while option not in ["y", "n"]:
        option = input("Please enter y or n only: ")
    return option


def quiz():
    number_of_question = 10
    score = 0
    operator_list = ["*", "+", "-"]

    print("You have 10 seconds to answer each question.\n"
          "Let's start!!")
    for counter in range(number_of_question):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        operator = random.choice(operator_list)
        question = f"#{counter}: {num1} {operator} {num2} = "
        correct_answer = answer(operator, num1, num2)

        try:
            pyip.inputNum(question, allowRegexes=[f'^{correct_answer}$'],
                          blockRegexes=[('.*?', f'Incorrect! The correct answer is {correct_answer}.')], timeout=10,
                          limit=1)
        except pyip.TimeoutException:
            print("Out of time!")
        except pyip.RetryLimitException:
            print("Next question")
        else:
            print("Correct\n"
                  "Next question")
            score += 1
        time.sleep(0.5)

    print(f"\nScores: {score}")
    while continue_game() != "n":
        quiz()
    print("\nThanks for playing!")


if __name__ == "__main__":
    quiz()

