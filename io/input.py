def reverse(text):
	return text[::-1]
def is_palindrome(text):
	return text == reverse(text)

sth = input("Enter text:")
if is_palindrome(sth):
	print("Yes ,it is a palindrome")
else:
	print("No,it is a palindrome")
