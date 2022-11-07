import prompt
from brain_games.cli import welcome_user


def launch(game):
    name = welcome_user()
    print(game.description)

    for _ in range(3):
        question, correct_answer = game.data_about_round()
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
