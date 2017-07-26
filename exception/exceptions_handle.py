try:
	text = input("Enter sth--->")
except EOFError:
	print('why did u do an EOF on me?')
except KeyboardInterrupt:
	print('U cancelled th operation.')
else:
	print('u enterd {}'.format(text))
