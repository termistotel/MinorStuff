import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

def gauss(xx,mu,sigma):
    a = np.exp(-np.square((xx-mu)/sigma)/2)
    N = np.sqrt(2*np.pi)*sigma
    return a/N

img = cv2.cvtColor(cv2.imread("0mask.png"), cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
edge = sobel.reshape(sobel.shape + (1,1))

rmax = int(np.sqrt(np.sum(np.square(img.shape))))
thetaNum = 50
rNum = 50
theta = np.linspace(-np.pi, np.pi, thetaNum).reshape(1, 1,1,-1)
radii = np.linspace(0, rmax, rNum).reshape(1, 1,-1,1)

sigma = 1

print(rmax)

xx, yy = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))
xx = xx.reshape(xx.shape + (1,1))
yy = yy.reshape(yy.shape + (1,1))

xx1 = (xx*np.cos(theta) + yy*np.sin(theta)).astype(np.int)
print("eto")
a = gauss(xx1, radii, 1)
print("eto2")

hough = np.sum(edge*a, axis=(0,1))

print(a.shape, hough.shape)

plt.imshow(hough)
plt.show()


tt, rr = np.meshgrid(theta, radii)

#hought = cv2.filter2D(hought, -1, np.ones((5,5))/25)
hmax = np.max(hough)

minTresh = 0.6
rs = rr[hough>(minTresh*hmax)]
ts = tt[hough>(minTresh*hmax)]

hx, hy = np.meshgrid(np.arange(hough.shape[1]), np.arange(hough.shape[0]))
hxs = hx[hough>(minTresh*hmax)]
hys = hy[hough>(minTresh*hmax)]

disp = np.zeros(img.shape[:2])

for r, t, x, y in zip(rs, ts, hxs, hys):
	# print((r,t))
	xx1 = (xx*np.cos(t) + yy*np.sin(t))
	clip = np.logical_and(xx1<r+1, xx1>r-1).reshape(xx1.shape[:2])
	disp[clip] += np.square(hough[y, x])

disp += sobel/np.max(sobel)*np.square(np.max(hough))

plt.imshow(disp)
plt.show()