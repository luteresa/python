import sys
import time

f = None
try:
	with open("poem.txt") as f:
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line,end='')
			sys.stdout.flush()
			print("Press ctrl+c now")
			time.sleep(2)
except IOError:
	print("coule not fine file poem.txt")
except KeyboardInterrupt:
	print("!!u cancelled the reading from the file.")
finally:
	if f:
		f.close()
	print("(Cleaning up: Closed th file)")
