import random

description = 'What is the result of the expression?'


def data_about_round():
	number1 = str(random.randint(1, 100))
	number2 = str(random.randint(1, 100))
	sign = random.choice(('+', '-', '*'))
	question = number1 + sign + number2
	correct_answer = str(calculatuon(question))
	return question, correct_answer


def calculatuon(value):
	return eval(value)