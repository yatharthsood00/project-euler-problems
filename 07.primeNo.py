lis = [2, 3, 5, 7, 11, 13]
print(len(lis))
print(lis)
for i in range(17,110000,2):
	if len(lis) == 10001:
		print(lis[10000])
		break
	for div in lis:
		if i % div == 0:
			break
		else:
			if div == lis[len(lis) - 1]:
				print("no added: ", i)
				lis.append(i)
			continue

