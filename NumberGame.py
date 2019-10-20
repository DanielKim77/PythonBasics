import random

Difficulty = input('Enter a difficulty: Easy, Medium, Hard, SupaEasy')
if Difficulty == "Easy":
	random_number = random.randint(0, 10) 

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
elif Difficulty == "Medium":
	random_number = random.randint(0,100)


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

elif Difficulty == "Hard":
	random_number = random.radint(0,1000)

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
elif Difficulty == "SupaEasy":
	guess = input('enter_number')
	guess = int(guess)
	print('correct!')
