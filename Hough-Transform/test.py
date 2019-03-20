import numpy as np
import cv2
import matplotlib.pyplot as plt

def gauss(xx,mu,sigma):
	a = np.exp(-np.square((xx-mu)/sigma)/2)
	N = np.sqrt(2*np.pi)*sigma
	return a/N


img = cv2.cvtColor(cv2.imread("black_cat.jpg"), cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
edge = sobel
# plt.imshow(img, cmap='gray')
# plt.show()

# plt.imshow(sobel, cmap='gray')
# plt.show()

size = np.square
rmax = int(np.sqrt(np.sum(np.square(img.shape))))
thetaNum = 50
rNum = 50
theta = np.linspace(0, np.pi/2, thetaNum)
radii = np.linspace(0, rmax, rNum)

hought = np.zeros((rNum, thetaNum))

sigma = 1

print(rmax)

xx, yy = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))

plt.imshow(xx)
plt.show()

for i, r in enumerate(radii):
	print(i)
	for j, t in enumerate(theta):
		xx1 = (xx*np.cos(t) + yy*np.sin(t)).astype(np.int)
		# yy1 = (-xx*np.sin(t) + yy*np.cos(t)).astype(np.int)
		a = gauss(xx1, r, sigma)
		hought[i,j] = np.sum(a*edge)

plt.imshow(hought)
plt.show()