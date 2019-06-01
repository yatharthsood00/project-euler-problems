sSq,sqS = 0,0
for i in range(1, 101):
	sSq = sSq + i*i
	sqS = sqS + i

sqS = sqS*sqS
print("square of sum", sqS)
print("sum of square", sSq)
print(sqS - sSq)