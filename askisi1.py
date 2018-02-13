import random
A=[[0 for j in range(5)] for i in range(100)]   #arxikopoieisi disdiastatou pinaka gia 100 paixtes pou exoun 5 arithmous
f = 0
for i in range(100) :                           #gemisma disdiastatou pinaka gia 100 paixtes pou exoun 5 arithmous
	for j in range(5) :
		if(j==0) :
			A[i][j] = random.randint(1,80)
		else :
			while 1 :                           #elenxos gia na min uparxoun idioi arithmoi
				A[i][j] = random.randint(1,80)
				for k in range(j) :
					if(A[i][j] == A[i][k]) :
						f = 1
				if(f==0) :					
					break
				else :
					f = 0
sum = 0
for i in range(1000) :
	B =[0 for i in range(80)]                      #arxikopoieisi monodiastatou pinaka gia ton an exoun bgi oi ariumoi apo tin klirotida 0 an oxo 1 an nai
	C =[0 for i in range(100)]                      #arxikopoieisi monodiastatou pinaka gia tous 100 paixtes pou apouhkeuete posi arithmi exoun bgi apo tos 5 tou kathenos apo tin kliritida
	f2 = 0
	p = 0
	while(f2 == 0) :
		while 1 :								#elenxos gia na min klirothoun idioi arithmoi
			x = random.randint(1,80)                
			if(B[x-1] == 0) :
				B[x-1] = 1				
				break
		p = p +1		
		for ii in range(100) : 
			f1 = 0
			for jj in range(5) :
				if(A[ii][jj] == x) :            #elenxos an uparxi o arithmos pou klirothike ston kathe pexti
					C[ii] = C[ii] +1					
					f1 = 1					
					break
			if(f1 == 1) :
				if(C[ii] == 5) :				#elenxos an brethike paixtis pou ekane bingo
					f2 = 1					
					break					
	sum = sum + p	
print "oi aeithmoi pou klirothikan mexri ta 1000 bingo einai : ",sum	
if(sum % 1000 <500) :		
	print "\no mesos oros ton arithomon pou prepei na bgoun gia na exoume bingo einai : " ,sum/1000	
else :
	print "\no mesos oros ton arithomon pou prepei na bgoun gia na exoume bingo einai : " ,sum/1000 + 1