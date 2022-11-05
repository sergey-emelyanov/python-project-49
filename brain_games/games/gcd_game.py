import random

description = 'Find the greatest common divisor of given numbers.'


def data_about_round():
	number1 = random.randint(1, 100)
	number2 = random.randint(1, 100)
	question = f"{number1} {number2}"
	correct_answer = str(nod(number1, number2))
	return question, correct_answer


def nod(number1, number2):
	multipliers1 = []
	for i in range(1, number1 + 1):
		if number1 % i == 0:
			multipliers1.append(i)

	multipliers2 = []
	for i in range(1, number2 + 1):
		if number2 % i == 0:
			multipliers2.append(i)

	set_of_both_multipliers = set(multipliers1) & set(multipliers2)
	return max(set_of_both_multipliers)
