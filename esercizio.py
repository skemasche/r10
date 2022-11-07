print ("1)Calcolare area cerchio\n 2)calcolare area quadrato\n 3)calcolarearea rettandolo\n")
x= int( input("Quale azione si vuole eseguire?"))
if(x==1):
	r = float( input("inserire il raggio:"))
	circonferenza=2*3.14*r
	print ("la circonferenza e':", circonferenza)
elif (x==2):
	lato = int (input("inserire la misura del lato"))
	p = 4*lato
	print (p)
elif (x==3):
	lat1 = int (input("inserire la misura del lato"))
	lat2 = int (input("inserire la misura del secondo lato"))
	peri = 2*( lat1 + lat2 )
	print("il perimetro e':", peri)
else:
	print("errore")
