import prompt


def welcome_user():
	name = prompt.string("May i have yur name?")
	print(f"Hello,{name}!")
