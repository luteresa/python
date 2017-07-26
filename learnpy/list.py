#codeing=utf-8
L = ['Bart','Lisa','Adam']
for item in L:
	print('Hello,',item,end='!')
	print('\r\n')

import os
l = [m+n for m in 'abcde' for n in 'xmyz']
print(l)
d={'x':'A','y':'B','z':'C'}
l2 = [k+'='+v for k,v in d.items()]
print(l2)
[s.lower() for s in l2]
print(l2)
