#specPythNew.py
 

limits = 1000
lis = []
c, m = 0, 2
   
while c < limits : 
          
    # Now loop on n from 1 to m-1 
    for n in range(1, m) : 
        a = m * m - n * n 
        b = 2 * m * n 
        c = m * m + n * n 
        # if c is greater than 
        # limit then break it 
        if c > limits : 
            break
  
        print(a, b, c)
        lis.append([a,b,c]) 
  
    m = m + 1

prod = 1

for i in lis:
	if sum(i) == 1000:
		print(i)
		for k in i:
			prod = prod * k
			print(prod)