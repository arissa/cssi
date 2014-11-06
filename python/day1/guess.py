import random
rand_num = random.randint(1,10)
guess1 = int(raw_input('Enter a number:\n'))
num_guesses = 1
if guess1 > 10 or guess1 < 1:
	print 'Not within range.'
else:
	if guess1 == rand_num:
		print 'You win!'
	else:
		print 'Guess again!'
		while num_guesses < 3:
			guess = int(raw_input('Enter a number:\n'))
			if guess > 10 or guess < 1:
				print 'Not within range.'
			else:
				if guess == rand_num:
					print 'You win!'
					break
				else:
					print 'Guess again!'
					num_guesses += 1
		