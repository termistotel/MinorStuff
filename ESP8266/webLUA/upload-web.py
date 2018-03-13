#!/usr/bin/env python
import sys
import os

def upload(uploadloc, loc):
	os.system("sudo python2 "+uploadloc+" upload "+loc)

def uploadall(uploadloc, loc):
	for file in os.listdir(loc):
		full = loc+"/"+file

		if os.path.isdir(full):
			uploadall(uploadloc, full)
		else:
			upload(uploadloc,full[2:])
			print full[2:]
			

if __name__== "__main__":
	args = sys.argv
	nodemcuLoc="./" #relativna lokacija programa za nodemcu za esp8266
	paths = os.environ["PATH"].split(os.pathsep) #env. varijabla path
	#paths = paths + os.environ["PYTHONPATH"].split(os.pathsep) #env. varijabla pythonpath
	lokacija = None

	for path in paths:
		if os.path.exists(path) and ("nodemcu-uploader.py" in os.listdir(path)): #trazi nodemcu-uploader.py u path varijabli
			print(path)
			lokacija = path+("/nodemcu-uploader.py").replace("//","/") #lokacija programa za uploadavanje

	if not lokacija:
		sys.exit("nema nodemcu-uploader.py u PATH ili PYTHONPATH varijablama")

	uploadall(lokacija, nodemcuLoc+"www")
