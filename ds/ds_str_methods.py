#This is a string object
name = 'Swaroop'

if name.startswith('Swaddd'):
	print("Yes, the string starts with 'Swa'")

if 'a' in name:
	print('Yes,it contains the string "a"')

if name.find('war') != -1:
	print("yes, it contains the string 'war'")

delimiter = '_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))
