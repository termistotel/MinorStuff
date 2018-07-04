import cv2
import numpy as np
import re, mmap

# img = cv2.imread("/home/alion/Desktop/PRAljAk.png", flags=cv2.IMREAD_COLOR)
# cv2.putText(img, "test" ,(419,351), 21, 1,(255,255,255),2,cv2.LINE_AA)

# cv2.imshow("slika",img)
# cv2.waitKey(0)


def temperature(put="/home/alion/Projekti/MinorStuff/Makro/makroTemp", dt = 0.1):
	with open(put, 'r+') as f:
		data = mmap.mmap(f.fileno(), 0)
		pattern = re.compile(r'Temp (.+?) ')

	temp = np.array([i for i in re.findall(pattern, data)])
	vrijeme = np.array([dt*i for i in range(temp.shape[0])])

	return (temp, vrijeme)

videoIn = cv2.VideoCapture('/home/alion/Videos/ML/Unsupervised/01Clustering - Unsupervise Learning: Introduction.mp4')
fps = videoIn.get(cv2.CAP_PROP_FPS)
fourcc = videoIn.get(cv2.CAP_PROP_FOURCC)
maxwidth = int(videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
maxheight = int(videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))

print cv2.VideoWriter_fourcc(*'H264')
print int(fourcc)

# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), int(fps), (maxwidth,maxheight))

# temp, vrijeme = temperature()

# frameno = 0
# while(videoIn.isOpened()):

#  	ret, frame = videoIn.read()

#  	indeks = np.sum(vrijeme< (frameno/fps))

#  	if ret and (indeks < len(temp)):
#  		cv2.putText(frame, temp[indeks], (419,351), 21, 1,(0,0,0),2,cv2.LINE_AA)
#  		cv2.imshow('frame',frame)

#  	if cv2.waitKey(1) & 0xFF == ord('q'):
#  		break

#  	out.write(frame)

#  	frameno += 1

# videoIn.release()
# out.release()
# cv2.destroyAllWindows()



cap = cv2.VideoCapture('/home/alion/Videos/ML/Unsupervised/01Clustering - Unsupervise Learning: Introduction.mp4')
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))))
for i in range(100):
    ret, frame = cap.read()        
    out.write(frame)
cap.release()
out.release()
