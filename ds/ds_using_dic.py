#'ab' is short for 'a' ddress 'b'ook
ab = {
	'Swaroop':'Swaroop@gmail.com',
	'larry':"larry@163.com",
	'Spyman':'spyman@hotmail.com'
	}
print("Swaroop's address is",ab['Swaroop'])

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
#deleting a key-value pair
del ab['larry']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
	print('Contact {} at {}'.format(name,address))

#adding a key-value pair
ab['Leon'] = 'leonyu@gmail.com'
if 'Leon' in ab:
	print("\n Leon's addr is",ab['Leon'])
