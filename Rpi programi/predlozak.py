#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import math

tonovi = {'C':16.35, 'Cis':17.32, 'D':18.35, 'Dis':19.45, 'E':20.60, 'F':21.83, 'Fis':23.12, 'G':24.50, 'Gis':25.96, 'A':27.50, 'Ais':29.14, 'H':30.87, 'C':32.70}

GPIO.setmode (GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

GPIO.output(14,False)

def sviraj (x,t):
	maks=int(math.floor(t*x))
	for i in range(maks):
		GPIO.output(14,True)
		GPIO.output(14,False)
		time.sleep(1/x)
	time.sleep(t-maks)

time.sleep(5)






