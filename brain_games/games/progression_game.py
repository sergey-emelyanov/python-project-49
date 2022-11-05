import random

description = 'What number is missing in the progression?'


def data_about_round():
	start = random.randint(1, 10)
	finish = start + 15
	step = random.randint(1, 3)
	index_arr = []
	for i in range(start, finish, step):
		index_arr.append(i)
	index = random.choice(index_arr)
	return make_progression(start, finish, step, index)


def make_progression(start, finish, step, index):
	question_arr = []
	correct_answer = 0
	for i in range(start, finish, step):
		if index == i:
			correct_answer = str(i)
			i = ".."
		question_arr.append(str(i))

	question = " ".join(question_arr)
	return question, correct_answer
