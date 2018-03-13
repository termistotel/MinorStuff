#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import math
import sys

tonovi = {'C':16.35, 'Cis':17.32, 'D':18.35, 'Dis':19.45, 'E':20.60, 'F':21.83, 'Fis':23.12, 'G':24.50, 'Gis':25.96, 'A':27.50, 'Ais':29.14, 'H':30.87}
playlista = (sys.argv)

GPIO.setmode (GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(14,False)
GPIO.output(15,False)
broj = 0
limit = 70
smjer = False
jed = 0.19
pauza = 0.03

def povecaj ():
	global broj
	global smjer
	broj = broj +1
	if (broj >= limit):
		smjer = not smjer
		GPIO.output(15,smjer)
		broj = 0

def sviraj (x,t):
	maks=int(math.floor((t-pauza)*x))
	for i in range(maks):
		GPIO.output(14,False)
		GPIO.output(14,True)
		povecaj()
		time.sleep(1.0/x)
#		GPIO.output(14,False)
	time.sleep(t-maks/x)

def sviraj1 (x,t):
	maks=int(math.floor(t*x))
	for i in range(maks):
		GPIO.output(14,True)
		povecaj()
		time.sleep(1.0/x)
		GPIO.output(14,False)

def provjera(r,l):
	for i in range(r):
		print('C')
		sviraj((2**i)*tonovi['C'], l)
		print('D')
	        sviraj((2**i)*tonovi['D'], l)
		print('E')
	        sviraj((2**i)*tonovi['E'], l)
	     	print('F')
		sviraj((2**i)*tonovi['F'], l)
		print('G')
	        sviraj((2**i)*tonovi['G'], l)
		print('A')
	        sviraj((2**i)*tonovi['A'], l)
		print('H')
	        sviraj((2**i)*tonovi['H'], l)

def kraj():
	while not ((broj == 0) and (smjer == False)):
		GPIO.output(14,True)
		GPIO.output(14,False)
		time.sleep(0.01)
		povecaj()

class ton:
	def __init__(self, ton, harm, duljina):
		self.ton = ton
		self.harm = int(harm)
		tmp = duljina.split('/')
		self.duljina = float(tmp[0])/float(tmp[1])

class pjesma:
	def __init__(self,fajl,jedd):
		self.jed = jedd
		f= open(fajl, 'r')
		tmp = f.read().split('\n')
		self.pesam=[]
		for i in tmp:
			if not(i==''):
				tmp1=i.split(' ')
				tonTmp = ton(tmp1[0],tmp1[1],tmp1[2])
				self.pesam.append(tonTmp)
	def tempo(self,jedd):
		self.jed = jedd
	def svirajBrate(self):
		for i in self.pesam:
			if i.ton == 'r':
				time.sleep(i.duljina*self.jed)
			else:
				sviraj((2**(i.harm))*tonovi[i.ton],i.duljina*self.jed)	


def kvinta (x,t):
        maks=int(math.floor(t*x/2))
        for i in range(maks):

                GPIO.output(14,False)
		GPIO.output(14,True)
                povecaj()
                time.sleep(1.0/(3*x))
		
		time.sleep(1.0/(3*x))
		GPIO.output(14,False)
                GPIO.output(14,True)
                povecaj()
                time.sleep(1.0/(3*x))
                GPIO.output(14,False)

                GPIO.output(14,True)
                povecaj()
                time.sleep(1.0/(3*x))
                GPIO.output(14,False)

                GPIO.output(14,True)
                povecaj()
                time.sleep(1.0/(3*x))
                GPIO.output(14,False)

                time.sleep(1.0/(3*x))

if playlista[1] == 'provjera':
	provjera(int(playlista[2]),float(playlista[3]))
else:
	pauza = float(playlista[2])
	for i in playlista[3:]:
		pesam = pjesma(i,int(playlista[1]))
		pesam.svirajBrate()


kraj()
