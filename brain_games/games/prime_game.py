import random

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def data_about_round():
	number = random.randint(1, 100)
	if is_prime(number):
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	return number, correct_answer


def is_prime(number):
	if number == 1:
		return False
	flag = True
	for i in range(2, int(number ** 0.5) + 1):
		if number % i == 0:
			flag = False
			break
	return flag
