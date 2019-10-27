import random

def PlayNumberGame():
	number_guessed = False
	while(number_guessed == False):
		guess = input('enter_number ')
		guess = int(guess)
		if guess == random_number:
			print(random_number)
			print('correct!')
			number_guessed = True
		elif guess < random_number:
			print('too low!')
		elif guess > random_number:
			print('too high!')

difficulty = input('Enter a difficulty: Easy, Medium, Hard, SupaEasy ')
if difficulty == "Easy":
	random_number = random.randint(0, 10) 
	PlayNumberGame()
elif difficulty == "Medium":
	random_number = random.randint(0,100)
	PlayNumberGame()
elif difficulty == "Hard":
	random_number = random.randint(0,1000)
	PlayNumberGame()
elif difficulty == "SupaEasy":
	guess = input('enter_number ')
	guess = int(guess)
	print('correct!')