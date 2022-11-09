import random

description = 'What number is missing in the progression?'


def data_about_round():
    start = random.randint(1, 10)
    finish = start + 20
    step = random.randint(1, 3)
    index_arr = []
    count = 0
    for i in range(start, finish, step):
        if count == 7:
            break
        index_arr.append(i)
        count += 1
    index = random.choice(index_arr)
    return make_progression(start, finish, step, index)


def make_progression(start, finish, step, index):
    question_arr = []
    correct_answer = 0
    count = 0
    for i in range(start, finish, step):
        if count == 7:
            break
        if index == i:
            correct_answer = str(i)
            i = ".."
        question_arr.append(str(i))
        count += 1

    question = " ".join(question_arr)
    return question, correct_answer
