import numpy as np
import cv2
import matplotlib.pyplot as plt

def gauss(xx,mu,sigma):
	a = np.exp(-np.square((xx-mu)/sigma)/2)
	N = np.sqrt(2*np.pi)*sigma
	return a/N


img = cv2.cvtColor(cv2.imread("0mask.png"), cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
edge = sobel
# plt.imshow(img, cmap='gray')
# plt.show()

# plt.imshow(sobel, cmap='gray')
# plt.show()

rmax = int(np.sqrt(np.sum(np.square(img.shape))))
thetaNum = 100
rNum = 100
theta = np.linspace(-np.pi, np.pi, thetaNum)
radii = np.linspace(0, rmax, rNum)

ymax, xmax = img.shape

hought = np.zeros((rNum, thetaNum))

sigma = 1

print(rmax)

xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
tt, rr = np.meshgrid(theta, radii)
plt.imshow(img)
plt.show()

xinit = np.ones(2*rmax)
yinit = np.arange(-rmax, rmax)

for i, r in enumerate(radii):
	print(i)
	for j, t in enumerate(theta):
		xs = (xinit*r*np.cos(t) - yinit*np.sin(t)).astype(np.int)
		ys = (xinit*r*np.sin(t) + yinit*np.cos(t)).astype(np.int)

		clip = np.logical_and(xs<xmax, ys<ymax)
		clip = np.logical_and(clip, xs>=0)
		clip = np.logical_and(clip, ys>=0)
		hought[i,j] = np.sum(edge[ys[clip], xs[clip]])

		# f = edge
		# f[ys[clip], xs[clip]] = np.max(f)
		# plt.imshow(f)
		# plt.show()

plt.imshow(hought)
plt.show()

# hought = cv2.resize(hought, (0,0), fx=1, fy=1)
theta = np.linspace(-np.pi, np.pi, hought.shape[1])
radii = np.linspace(0, rmax, hought.shape[0])
tt, rr = np.meshgrid(theta, radii)

print(theta)
print(radii)
print(rr.shape, radii.shape)
print(tt.shape, theta.shape)

#hought = cv2.filter2D(hought, -1, np.ones((5,5))/25)
hmax = np.max(hought)
rs = rr[hought>(0.8*hmax)]
ts = tt[hought>(0.8*hmax)]

disp = np.zeros((ymax, xmax))

for r, t in zip(rs, ts):
	print((r,t))
	xx1 = (xx*np.cos(t) + yy*np.sin(t))
	clip = np.logical_and(xx1<r+0.5, xx1>r-0.5)
	disp[clip] = 1

plt.imshow(hought)
plt.show()

plt.imshow(sobel)
plt.show()

plt.imshow(disp)
plt.show()