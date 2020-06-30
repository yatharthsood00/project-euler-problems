import itertools
import time
start_time = time.time()
for i in itertools.count(100000,20):
	for div in range(2, 21):
		if i % div == 0:
			if div == 20:
				print("number", i)
				print("%s seconds" % (time.time() - start_time))
				quit()
			continue
		else:
			#print(i, ":no")
			break

