import os
print('Precess (%s) start...'%os.getpid())
pid = os.fork()
if pid == 0:
	print('Iam child precess (%s) and my parent is %s.'%(os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child precess (%s)'%(os.getpid(),pid))
