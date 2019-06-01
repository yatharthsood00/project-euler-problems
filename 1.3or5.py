i = 0
lis = []
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		lis.append(i)
print(sum(lis))
