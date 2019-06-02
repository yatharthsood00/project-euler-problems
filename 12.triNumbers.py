import itertools
from bisect import bisect_right
lis = []
sLis = []
thisVal = 1000
for i in itertools.count(1):
	lis.append(i)
	if i == thisVal:
		break
for k in range(len(lis)):
	if k > 0:
		sLis.append(sLis[k - 1] + lis[k])
	else:
		sLis.append(1)
for x in range(thisVal,sLis[len(sLis) - 1]):
	lis.append(x)


hiFactors = 0
hiFVal = None
currFacList = []
i = None
for i in sLis:
	#print("for %s ", i)
	for j in lis[0:bisect_right(lis, i)]:
		if i % j == 0:
			currFacList.append(j)
			#print(j)
		if j == lis[bisect_right(lis, i) - 1]:
			if currFacList[len(currFacList) - 1] != i:
				currFacList.append(i)
			#print("no of prime factors = ", len(currFacList))
			#print(currFacList)
			if hiFactors < len(currFacList):
				hiFactors = len(currFacList)
				hiFVal = i
				print("New highest: ", hiFactors)
				print("New highest at: ", hiFVal)
			if hiFactors == 5:
				print("Found at: ")
				print(hiFVal)
				quit()
			#print(currPrimeList)
	currFacList = []
	j = None	

print("\n \nthus: ")
print(hiFactors)
print(hiFVal)
