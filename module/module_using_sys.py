import sys
import os
print('the command line arguments are:')
for i in sys.argv:
	print(i)

print('\n\nThe PYTHONPATH is', sys.path,'\n')
print(os.getcwd())
for item in sys.path:
	print(item)
from math import sqrt
print('Squre root of 16 is ',sqrt(16))
