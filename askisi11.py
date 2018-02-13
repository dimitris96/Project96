import random
A=[[0 for j in range(100)] for i in range(100)]   #arxikopoieisi disdiastatou pinaka
for i in range(100) : 
	for j in range(100) :
		A[i][j] = chr(random.randint(65,90))
fl2 = 0		                                   #flag esto an brethike mia sosti leksi ston pinaka
x = input("dose onoma arxiou : ")
f = open(x , "r")	
while 1 :
	ln = f.readline() 
	l = len(ln)	
	if(l == 0) :
		break
	line = ""
	for i in range(l-1) :                     #sozo tin grammi se neo string oste na sbiso tin allagis grammis gia na ginei sosta h sigrisi 
		line = line + ln[i]
	l = l - 1		
	fl1 = 0	                                   #flag an i sugekrimeni leksi exei brethi  
	for i in range(100)	:
		for j in range(100-l+1) :              #psanxo tin leksi orizodia ana grammi
			y = ""
			for k in range(j,j+l) :
				y = y + A[i][k]
			if(cmp(y, line)  == 0)	:
				print "iparxi h leksi : ",line
				fl1 = 1
				fl2 = 1
				break
		if(fl1 == 1)	:	
			break
	if(fl1 == 0)		:
		for i in range(100-l+1)	:             #psanxo tin leksi kathena ana stili
			for j in range(100) :                
				y = ""
				for k in range(i,i+l) :
					y = y + A[k][j]
				if(cmp(y, line)  == 0)	:
					print "iparxi h leksi : ",line
					fl1 = 1
					fl2 = 1
					break
			if(fl1 == 1)	:		
				break
f.close()				
if(fl2 == 0) :
	print "den brethike kamia leksi na iparxei ston pinaka"