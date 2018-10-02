import cv2
import numpy as np
# import re, mmap

tempFile="/home/alion/Projekti/MinorStuff/Makro/makroTemp"
inputVideo='/media/alion/New Volume/NSA/NSA_3.avi'
outputVideo='output.avi'
dt = 0.298
display = False

# Ova funkcija vadi temperature iz fajla i izracunava u koje vrijeme je koja temperatura zabiljezena
def temperature(put=tempFile, dt = dt):
	f = open(put, 'r', encoding="ISO-8859-1")
	
	pattern = re.compile(r'Temp (.+?) ')
	temp = np.array([i for i in re.findall(pattern, f.read())])
	vrijeme = np.array([dt*i for i in range(temp.shape[0])])

	print("Duljina vremena skupljanja podataka o temperaturi: "+ "{0:.1f}".format(temp.size*dt))

	return (temp, vrijeme)


# Sranja s inicijaliziranjem
videoIn = cv2.VideoCapture(inputVideo)
fps = videoIn.get(cv2.CAP_PROP_FPS)
fourcc = videoIn.get(cv2.CAP_PROP_FOURCC)
maxwidth = int(videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
maxheight = int(videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))

# print(cv2.VideoWriter_fourcc(*'XVID'))
# print(int(fourcc))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Inicijaliziraj output video
out = cv2.VideoWriter(outputVideo, int(fourcc), int(fps), (maxwidth,maxheight))

# Vektori s temperaturama i vremenom
temp, vrijeme = temperature()



# Glavna petlja koja stavlja temperaturu na svaki frame

videoLength = videoIn.get(cv2.CAP_PROP_FRAME_COUNT)/fps
frameno = 0
while(videoIn.isOpened()):

	ret, frame = videoIn.read()

	indeks = np.sum(vrijeme < (frameno/fps))

	if ret and (indeks < len(temp)):
		cv2.putText(frame, temp[indeks], (maxwidth - 100,maxheight - 20), 21, 1,(0,255,0),2,cv2.LINE_AA)
		
		if display:
			cv2.imshow('frame',frame)
	if display:
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# if int(100*videoIn.get(cv2.CAP_PROP_POS_AVI_RATIO))%10 == 0:

	if frameno%1000 == 0:
		progress = 100*videoIn.get(cv2.CAP_PROP_POS_MSEC)/1000/videoLength
		print("progress: "+"{0:.1f}".format(progress))

	out.write(frame)

	frameno += 1

videoIn.release()
out.release()
cv2.destroyAllWindows()

print("Gotovo")