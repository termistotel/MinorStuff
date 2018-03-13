#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(23,False)
GPIO.output(24,False)

raw_input("Upali")
GPIO.output(24,True)

raw_input("Ugasi")
GPIO.output(24,False)

