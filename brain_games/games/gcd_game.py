import random

description = 'Find the greatest common divisor of given numbers.'


def data_about_round():
	number1 = random.randint(1, 100)
	number2 = random.randint(1, 100)
	question = f"{number1} {number2}"
	correct_answer = str(nod(number1, number2))
	return question, correct_answer


def nod(number1, number2):
	while number2 > 0:
		number1, number2 = number2, number1 % number2
	return number1
