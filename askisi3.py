x = input("dose keimeno : ")                            #apothikeuo to string pou dinei o xristis
pl = len(x)
a =[0 for i in range(pl)]
for i in range(pl) :
	if(ord(x[i]) >=65 and ord(x[i]) <=90) :              #kano tin metatropi gia ta kefalaia
		a[i] = chr((ord(x[i]) - 65 + 13 )% 26 + 65)
	elif(ord(x[i]) >=97 and ord(x[i]) <=122) :           #kano tin metatropi gia ta mikra
		a[i] = chr((ord(x[i]) - 97 + 13 )% 26 + 97)
	else :
		a[i] = x[i]
x = ""		
for i in range(pl) :
	x = x + a[i]
print "me kriptografisi ROT13 einai :",x