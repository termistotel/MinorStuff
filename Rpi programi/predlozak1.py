#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import math

tonovi = {'C':16.35, 'Cis':17.32, 'D':18.35, 'Dis':19.45, 'E':20.60, 'F':21.83, 'Fis':23.12, 'G':24.50, 'Gis':25.96, 'A':27.50, 'Ais':29.14, 'H':30.87, 'C':32.70}

GPIO.setmode (GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(14,False)
GPIO.output(15,False)
broj = 0
limit = 80
smjer = False
jed = 0.19

def povecaj ():
	global broj
	global smjer
	broj = broj +1
	if (broj >= limit):
		smjer = not smjer
		GPIO.output(15,smjer)
		broj = 0

def sviraj (x,t):
	maks=int(math.floor(t*x))
	for i in range(maks):
		GPIO.output(14,True)
		povecaj()
		print (1.0/x)
		time.sleep(1.0/x)
		GPIO.output(14,False)
	time.sleep(t-maks/x)



#time.sleep(5)



def somberIntro ():
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['H'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['G'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['H'],jed)
	sviraj(4*tonovi['E'],jed)

	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['H'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['A'],jed)
	sviraj(4*tonovi['Fis'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(3*tonovi['D'],jed)

	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['H'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['G'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(4*tonovi['G'],jed)
	sviraj(4*tonovi['A'],jed)

	sviraj(4*tonovi['H'],jed)
	sviraj(8*tonovi['Cis'],jed)
	sviraj(8*tonovi['D'],jed)
	sviraj(4*tonovi['H'],jed)

	sviraj(4*tonovi['A'],jed)
	sviraj(4*tonovi['Fis'],jed)
	sviraj(4*tonovi['E'],jed)
	sviraj(3*tonovi['D'],jed)
while True:
	somberIntro()
#sviraj(150,10)

while not ((broj == 0) and (smjer == False)):
	GPIO.output(14,True)
	GPIO.output(14,False)
	time.sleep(0.01)
	povecaj()
