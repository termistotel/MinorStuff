#!/usr/bin/env python

import socket
import curses
from time import sleep

def povecaj(brzina,broj):
	if (brzina < 0) and (brzina > -broj):
		return 0
	br = brzina + broj
	if br > 1023:
		return 1023
	return br

def smanji(brzina,broj):
	if (brzina > 0) and (brzina < broj):
		return 0
	br = brzina - broj
	if br < -1024:
		return -1024
	return br

def glavni():
	global brzina
	global s

	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)

	stdscr.addstr(0,10,"Hit 'q' to quit")
	stdscr.refresh()

	key = ''
	while key != ord('q'):
		sleep(0.1)
		key = stdscr.getch()
		#stdscr.addch(20,25,key)
		stdscr.refresh()
		stdscr.addstr(2, 20, "     ")
		if key == curses.KEY_UP:
			brzina = povecaj(brzina,100)
			stdscr.addstr(2, 20, str(brzina))
			s.send(str(brzina))
		elif key == curses.KEY_DOWN: 
			brzina = smanji(brzina,100)
			stdscr.addstr(2, 20, str(brzina))
			s.send(str(brzina))

	curses.endwin()


TCP_IP = '192.168.4.1'
TCP_PORT = 6666
BUFFER_SIZE = 32
MESSAGE = ""

brzina = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#glavni()
while 1:
	data = raw_input("data: ")
	s.send(data)
s.close()
