import time
from bisect import bisect_right
from math import sqrt

start_time = time.time()
def sievesum(n):
	arr = [True for i in range(n+1)]
	p = 2
	while p**2 <= n:

		if arr[p] == True:
			for i in range(p*2,n+1,p):
				arr[i] = False
		p = p + 1
	
	prime = []

	for p in range(2,n):
		if arr[p]:
			prime.append(p)
	
	return sum(prime)

#lis = [2, 3, 5, 7, 11, 13]
#for i in range(17,2000000,2):
#	for div in lis:
#		if i % div == 0:
#			break
#		elif div == lis[bisect_right(lis, i//2)]:
#			print("no added: ", i)
#			print("currently %s seconds" % (time.time() - start_time))
#			lis.append(i)
#			break

#print(lis)
print(sievesum(2000000))

print("%s seconds" % (time.time() - start_time))