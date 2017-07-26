from multiprocessing import Process
import os
import time

def run_proc(name):
	print('Run child precess %s.(%s)'%(name,os.getpid()))
	print('sleep  for sec...')
	time.sleep(5)

if __name__=='__main__':
	print('Parent precess %s.'%os.getpid())
	p = Process(target=run_proc,args=('test',))
	print('Child precess will start.')
	p.start()
	p.join()
	print('Child precess end.')
