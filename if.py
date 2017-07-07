number=23

guess = int(input('Enter an integer: '))
if guess == number:
	print('Congratulations, u guessed it.')
	print('(but u do not win any prizes!)')
elif guess < number:
	print('No, it is l little higher than that')
else:
	print('No, it is a little lower than that')
print('Done')
if True:
	print('Yes, it is true')
