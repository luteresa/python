class Person:
	def __init__(self, name):
		self.name = name
		print(self.name)

	def say_hi(self):
		print('hello, my name is',self.name)

p = Person('aaaaa')
#p.say_hi()
