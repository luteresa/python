while True:
	s = input('Enter sth:')
	if s == 'quit':
		break
	if len(s) < 3:
		print('too small')
		continue
	print('Input is of sufficent legnth')
