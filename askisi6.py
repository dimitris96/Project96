sum = 0                              # sozoume poses meres brosta h piso eimaste apo tin afetiria se sxesi apo to mina kai to etos pou edose o xristis
arxi = 2017                          # etos san afetiria bazo 1/1/2017 pou einai i kiriaki
etos = input("dose etos : ")         # metabliti pou tha sothi to etos pou tha dosi o xristis
A = ["January", "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October", "November" , "December"]
minas = input("dose mina apo 1 mexri 12 : ") # metabliti pou tha sothi o minas pou tha dosi o xristis se morfi kanoniki me to onoma toy sta latinika 

while (minas < 1 or minas >12) :         # elenxos mexri na dosei egkiro mina	
	print "edoses lathos onoma mina"
	minas = input("dose jana mina apo 1 mexri 12: ") 	
		
if((etos - arxi) >= 0) :              # ama dosi etos megalitero apo tin afetiria	
	for i in range(arxi,etos) :		  # briski poses meres apexi i 1/1/ tou etous pou edose apo tin afetiria , bazo thn metebliti <etos> epidi to for metrai mexri ena ligotero pou thelo 	
		if(i % 4 != 0) :		
			sum = sum + 365			
		else :		
			sum = sum + 366				
	for i in range(2,minas+1) :	         # upologizo tin 1 tou minos pou exei dosei o xristis , bazo <minas +1> epidi thelo na upologiso kai ton idio ton mina
		if(i == 2 or i == 4 or i == 6 or i == 9 or i == 11 or i ==8) :	
			sum = sum + 31		
		elif(i == 5 or i == 7 or i == 10 or i == 12) :		
			sum = sum + 30		
		else :		
			if(etos % 4 != 0) :			
				sum = sum + 28			
			else :			
				sum = sum +29		
	mera = sum % 7                      # sozo tin imera tis protis tou minos pou edose o xristis sto etos pou edose	
else :	                                 # ama dosi etos mikrotero apo tin afetiria
	for i in range(arxi-1,etos-1,-1) :   # briski poses meres apexi i 1/1/ tou etous pou edose apo tin afetiria , bazo thn metebliti <etos-1> epidi to for metrai mexri ena parapano kai ego thelo mexri kai to etos pou dinei o xrisris
		if(i % 4 != 0) :		
			sum = sum + (-365)			
		else :		
			sum = sum + (-366)		
	for i in range(2,minas+1) :	  # upologizo tin 1 tou minos pou exei dosei o xristis , bazo <minas +1> epidi thelo na upologiso kai ton idio ton mina
		if(i == 2 or i == 4 or i == 6 or i == 9 or i == 11 or i ==8) :	
			sum = sum + 31		
		elif(i == 5 or i == 7 or i == 10 or i == 12) :		
			sum = sum + 30		
		else :		
			if(etos % 4 != 0) :			
				sum = sum + 28			
			else :			
				sum = sum +29				
	mera = sum % 7                 # sozo tin imera tis protis tou minos pou edose o xristis sto etos pou edose , briski tin sosti mera an kai to sum einai arnitiko
	
	# ftiaxno to imerologio
	
if(minas == 1 or minas == 3 or minas == 5 or minas == 7 or minas == 8 or minas == 10 or minas ==12)	:	
	if(mera == 0) :
		B = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","","","","","","",""]
	elif(mera == 1)	:	
		B = ["","01","02","03","04","05","06","07","08","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","","","","","",""]
	elif(mera == 2)	:	
		B = ["","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","","","","",""]
	elif(mera == 3) :
		B = ["","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","","","",""]
	elif(mera == 4)	:	
		B = ["","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","","",""]
	elif(mera == 5)	:	
		B = ["","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","","",""]	
	else :	
		B = ["","","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","","","","",""]		
elif(minas == 4 or minas == 6 or minas == 9 or minas == 11) :
	if(mera == 0) :
		B = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","","","","","","",""]
	elif(mera == 1)	:	
		B = ["","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","","","","","",""]
	elif(mera == 2)	:	
		B = ["","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","","","","",""]
	elif(mera == 3) :
		B = ["","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","","","",""]
	elif(mera == 4)	:	
		B = ["","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","","",""]
	elif(mera == 5)	:	
		B = ["","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","","",""]	
	else	:	
		B = ["","","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","","","","","",""]	
else :
	if(etos % 4 != 0) :								
		if(mera == 0) :
			B = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","","","","","","",""]
		elif(mera == 1)	:	
			B = ["","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","","","","","",""]
		elif(mera == 2)	:	
			B = ["","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","","","","",""]
		elif(mera == 3) :
			B = ["","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","","","",""]
		elif(mera == 4)	:	
			B = ["","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","","",""]
		elif(mera == 5)	:	
			B = ["","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","","",""]	
		else :		
			B = ["","","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","","","","","","","",""]		
	else :			
		if(mera == 0) :
			B = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","","","","","","",""]
		elif(mera == 1)	:	
			B = ["","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","","","","","",""]
		elif(mera == 2)	:	
			B = ["","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","","","","",""]
		elif(mera == 3) :
			B = ["","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","","","",""]
		elif(mera == 4)	:	
			B = ["","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","","",""]
		elif(mera == 5)	:	
			B = ["","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","","",""]	
		else	:	
			B = ["","","","","","","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","","","","","","",""]	
print A[minas-1],etos	
print "S\tM\tT\tW\tT\tF\tS"	
for i in range(0,42,7) :
	print B[i],"\t",B[i+1],"\t",B[i+2],"\t",B[i+3],"\t",B[i+4],"\t",B[i+5],"\t",B[i+6]
	
