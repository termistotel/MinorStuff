#!/usr/bin/python
from bitarray import bitarray
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(23,False)
GPIO.output(24,False)
o23 = False
o24 = False
prazno = bitarray()

upisi = bitarray('010000')
pc = bitarray('011000')
prog1 = bitarray('000100')
brisi = bitarray('100100')
#vrijeme = 0.00000001
vrijeme = 0.0001

def upisiSve(fajl):
	f = open(fajl,'r')
	tmp = bitarray()
	tmp.fromfile(f)
	for i in range(8192):
		if not (tmp == prazno):
			komanda(upisi,zaUpis(tmp[:14]))
			tmp = tmp[14:]
			komanda(prog1)
		komanda(pc)
def obrisiSve():
	for i in range(8192):
		komanda(brisi)
		komanda(pc)

def ping():
	GPIO.output(23,True)
	time.sleep(vrijeme/2)
	GPIO.output(23,False)
	time.sleep(vrijeme/2)

def uberTest():
	komanda(bitarray('001000'))

	print "Pocinje"

	for i in range(16):
		ping()
		print i
		time.sleep(0.5)

def zaUpis(podaci):
	a = bitarray('0')
	a.extend(podaci)
	a.append(False)
	return a

def komanda(naredba,*podaci):
	for i in naredba:
		ukucaj(i)
	time.sleep(vrijeme)
	for i in podaci:
		for j in i:
			ukucaj(j)
	if (naredba == prog1) or (naredba == pc):
		time.sleep(vrijeme*30)
	if (naredba == brisi):
		time.sleep(vrijeme*30)
		
def ukucaj(n):
	if n:
		jedan()
	else:
		nula()
def nula():
	global o24
	if o24:
		time.sleep(vrijeme/2)
		GPIO.output(24,False)
		o24=False
		time.sleep(vrijeme/2)
	ping()
def jedan():
	global o24
	if not o24:
		time.sleep(vrijeme/2)
		GPIO.output(24,True)
		o24=True
		time.sleep(vrijeme/2)
	ping()

def led():
	komanda(upisi,zaUpis(bitarray('11000000000000')))
	komanda(prog1)
	komanda(pc)

	komanda(upisi,zaUpis(bitarray('01011010000011')))
	komanda(prog1)
	komanda(pc)

	komanda(upisi,zaUpis(bitarray('00000010000101')))
	komanda(prog1)
	komanda(pc)

	komanda(upisi,zaUpis(bitarray('01001010000011')))
	komanda(prog1)
	komanda(pc)
	
	komanda(upisi,zaUpis(bitarray('11000000000000')))
	komanda(prog1)
	komanda(pc)
	
	komanda(upisi,zaUpis(bitarray('00000010000101')))
	komanda(prog1)
	komanda(pc)

        komanda(upisi,zaUpis(bitarray('10100000000110')))
        komanda(prog1)
        komanda(pc)

        komanda(upisi,zaUpis(bitarray('10100000000110')))
        komanda(prog1)
#        komanda(pc)

#komanda(pc)

#obrisiSve()
#print sad
#upisiSve('testfile')
#led()
uberTest()
komanda(pc)

#GPIO.output(24,True)
