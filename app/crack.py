#encodeing = utf-8
import os
import sys
import hashlib
import time
from datetime import datetime

def get_md5_value(src):
	m = hashlib.md5()
	m.update(src.encode('UTF-8'))
	return m.hexdigest()

def read_obj():
	pwd=input("Enter word:")
	return str(pwd)
def crack(x):
	x_md5 = get_md5_value(x)
	print(x_md5)
	i = 0
	for i in range(1,9999999999):
	#	md5=get_md5_value(str(i))
	#	if md5 == x_md5:
		if str(i) == x:
			print(i)
			return 0;
	return -1;

if __name__ == '__main__':
	obj=read_obj()
	a=datetime.now()
	print(a)
	flag = crack(str(obj))
	if flag==0:
		print ('crack sucess')
	else:
		print ('crack failed')

	b=datetime.now()
	print(b)

	print("run time:%s"%(b-a))
