import socket
import os

ip = input("Inserire indirizzo ip: ")
porta =int( input("\n inserire porta:"))
npak = int( input("\n inserire il numero di pacchetti da inviare:"))
bytes = os.urandom(1024)
puntapak= int(0)
while 1 == 1:
	try:
		if puntapak > npak:
			quit()
		else:
			socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			socket.sendto(bytes,(ip, porta))
			puntapak = puntapak+1
			print (puntapak, ip, porta)
	except KeyboardInterrupt:
		print ("stop")
		quit()
