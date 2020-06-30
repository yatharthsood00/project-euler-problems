lis = []
for i in range(100, 1000):
	for j in range(100, 1000):
		prod = i*j
		prodS = str(prod)
		prodS.split()
		if prod / 100000 == 0:
			continue
			#if prodS[0] == prodS[4]:
			#	if prodS[1] == prodS[3]:
			#		lis.append(prod)
			#		print(prod)
		else:
			if prod < 100000:
				continue
			elif prodS[0] == prodS[5]:
				if prodS[1] == prodS[4]:
					if prodS[2] == prodS[3]:
						lis.append(prod)
						#print(prod)
print("max: ", max(lis))
