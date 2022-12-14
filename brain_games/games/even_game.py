import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    number = random.randint(1, 100)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
