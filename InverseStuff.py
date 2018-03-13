import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy.signal import fftconvolve

def toGray(P):
	#print P.dtype
	return np.sum(P/(3.0*255), axis=2, dtype="float64")

def FTransPic(P, grid=None, dx=None):
	freq = []
	if dx==None:
		dx = 1

	if grid==None:
		for i in range(P.ndim):
			x = np.linspace(0, P.shape[i]-1, P.shape[i])
			xt = np.fft.fftfreq(x.size, dx)
			freq.append(xt)

		#grid = np.meshgrid(x,y)
	FT = np.fft.fftn(P)

	return FT, freq

def conv1(P, ker):
	return fftconvolve(P, ker, mode='same')

def conv2(P, ker):
	tmp = np.zeros(shape=(P.shape))
	tmp[:ker.shape[0], :ker.shape[1]] += ker

	ftp,_ = FTransPic(P)
	ftmp,_ = FTransPic(tmp)

	return np.real(np.fft.ifftn(ftp*ftmp))

x = np.linspace(0, 10*np.pi, 20)
y = np.linspace(0, 10*np.pi, 20)
x1 = np.array([np.sin(x)])
y1 = np.array([np.sin(y)])
A = y1.T.dot(x1)

#ft, freq = FTransPic(x1)

#plt.plot(freq[0],np.abs(ft))
#plt.show()

img = cv2.imread('res/black_cat.jpg')
img = toGray(img)

ker = np.ones((3,3))/25.0
ret = conv1(img,ker)
ret2 = conv2(img,ker)

print ret.dtype
print ret2.dtype

cv2.imshow('img', img)
cv2.waitKey(0)

cv2.imshow('img', ret2)
cv2.waitKey(0)

cv2.imshow('img', ret)
cv2.waitKey(0)











# B = np.fft.fft2(A)
# #B1 = np.sqrt(np.square(np.real(B)) + np.square(np.imag(B)))
# B1 = np.abs(B)

# #B[:B.shape[0]/2,:] = B[B.shape[0]/2:,:]

# C = np.fft.ifft2(B)

# # print np.real(B)

# cv2.imshow("img", A)
# cv2.waitKey(0)
# cv2.imshow("img", B1/10)
# cv2.waitKey(0)

# n = B1.shape[0]/2
# m = B1.shape[1]/2

# gore = np.hstack((B1[-n:,-m:], B1[-n:,:m]))
# dole = np.hstack((B1[:n, -m:], B1[:n,:m]))

# cv2.imshow("img", np.vstack((gore,dole))/10)
# cv2.waitKey(0)
# cv2.imshow("img", np.real(C))
# cv2.waitKey(0)
# cv2.imshow("img", A)
# cv2.waitKey(0)
# cv2.destroyAllWindows()