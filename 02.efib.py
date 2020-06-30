f = [0, 1]
i = 2
sum = 0
while f[i - 1] < 4000000:	
		f.insert(i, f[i-1] + f[i-2])
		if f[i] % 2 == 0:
				sum = sum + f[i]
		i = i + 1
print(sum)	

