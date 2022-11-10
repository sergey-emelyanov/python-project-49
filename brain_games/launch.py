import prompt


def launch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    for _ in range(3):
        question, correct_answer = game.get_game()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct")
        else:
            print(
                f"Answer {answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
