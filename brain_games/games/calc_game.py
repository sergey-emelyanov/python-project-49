import random

description = 'What is the result of the expression?'


def data_about_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    sign = random.choice(('+', '-', '*'))
    question = f"{str(number1)} {sign} {str(number2)}"
    correct_answer = str(calculatuon(number1, number2, sign))
    return question, correct_answer


def calculatuon(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
