import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

def gauss(xx,mu,sigma):
    a = np.exp(-np.square((xx-mu)/sigma)/2)
    N = np.sqrt(2*np.pi)*sigma
    return a/N


image = cv2.cvtColor(cv2.imread("0mask.png"), cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

x, y = image.shape

rmax = int(np.sqrt(np.sum(np.square(image.shape))))
thetaNum = 10
rNum = 10
theta = np.linspace(-np.pi, np.pi, thetaNum).reshape(1, -1, 1)
cost = np.cos(theta)
sint = np.sin(theta)

radii = np.linspace(0, rmax, rNum).reshape(-1, 1, 1)

sobelx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobely = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

xinit = np.ones((1, 1, 2*rmax))
yinit = np.arange(-rmax, rmax).reshape(1, 1, -1)

x1 = xinit*cost*radii - yinit*sint
y1 = xinit*sint*radii + yinit*cost

graph1 = tf.Graph()
with graph1.as_default():
    img = tf.constant(image.reshape(1,x,y,1), dtype=tf.float32)
    hough = tf.Variable(np.zeros((rNum, thetaNum)), dtype=tf.float32, trainable=False)

    sx = tf.constant(sobelx.reshape(3,3,1,1), dtype=tf.float32)
    sy = tf.constant(sobely.reshape(3,3,1,1), dtype=tf.float32)

    dx = tf.nn.convolution(img, sx, "SAME")
    dy = tf.nn.convolution(img, sy, "SAME")

    edges = tf.sqrt(tf.square(dx) + tf.square(dy))

    for i in range(len(x1)):
        for j, coords in enumerate(zip(x1[i], y1[i])):
            x11 = tf.cast(coords[0], tf.int32)
            y11 = tf.cast(coords[1], tf.int32)

            clipMax = tf.logical_and(x11<x, y11<y)
            clipMin = tf.logical_and(x11>=0, y11>=0)
            clip = tf.logical_and(clipMax, clipMin)

            # xc = x11[clip]
            # yc = y11[clip]
            
            xc = tf.boolean_mask(x11, clip)
            yc = tf.boolean_mask(y11, clip)

            print(i,j, hough)

            # tmp1 = edges[0, yc, xc, 0]
            tmp1 = tf.gather(edges[0], yc, axis=0)
            tmp1 = tf.gather(tmp1, xc, axis=0)[0]
            tmp = tf.reduce_sum(tmp1)
            hough[i,j].assign(tmp)

# graph1 = tf.Graph()
# with graph1.as_default():
#     img = tf.constant(image.reshape(1,x,y,1), dtype=tf.float32)
#     hough = tf.Variable((rNum, thetaNum), dtype=tf.float32)

#     for i, val in enumerate(zip(x1, y1)):
#         for j, coords in enumerate(val):


#     sx = tf.constant(sobelx.reshape(3,3,1,1), dtype=tf.float32)
#     sy = tf.constant(sobely.reshape(3,3,1,1), dtype=tf.float32)

#     dx = tf.nn.convolution(img, sx, "SAME")
#     dy = tf.nn.convolution(img, sy, "SAME")

#     edges = tf.sqrt(tf.square(dx) + tf.square(dy))

#     for i, r in enumerate(radii):
#         xs = tf.matmul(xinit*r, tf.transpose(cost)) - tf.matmul(yinit, tf.transpose(sint))
#         ys = tf.matmul(xinit*r, tf.transpose(sint)) - tf.matmul(yinit, tf.transpose(cost))


#     # for i, r in enumerate(radii):
#     #     for j, t in range(theta):
#     #         hough = hough[i, j].assign()

# with tf.Session(graph=graph1) as sess:
#     plt.imshow(sess.run(edges)[0,:,:,0], cmap='gray')
#     plt.show()


# sobel = np.sqrt(np.square(sobelx) + np.square(sobely))
# edge = sobel
# # plt.imshow(img, cmap='gray')
# # plt.show()

# # plt.imshow(sobel, cmap='gray')
# # plt.show()

# size = np.square
# rmax = int(np.sqrt(np.sum(np.square(img.shape))))
# thetaNum = 100
# rNum = 100
# theta = np.linspace(-np.pi, np.pi, thetaNum)
# radii = np.linspace(0, rmax, rNum)

# ymax, xmax = img.shape

# hought = np.zeros((rNum, thetaNum))

# sigma = 1

# print(rmax)

# xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
# tt, rr = np.meshgrid(theta, radii)
# plt.imshow(xx)
# plt.show()

# xinit = np.ones(2*rmax)
# yinit = np.arange(-rmax, rmax)

# for i, r in enumerate(radii):
#   print(i)
#   for j, t in enumerate(theta):
#       xs = (xinit*r*np.cos(t) - yinit*np.sin(t)).astype(np.int)
#       ys = (xinit*r*np.sin(t) + yinit*np.cos(t)).astype(np.int)

#       clip = np.logical_and(xs<xmax, ys<ymax)
#       clip = np.logical_and(clip, xs>=0)
#       clip = np.logical_and(clip, ys>=0)
#       hought[i,j] = np.sum(edge[ys[clip], xs[clip]])

#       # f = edge
#       # f[ys[clip], xs[clip]] = np.max(f)
#       # plt.imshow(f)
#       # plt.show()

# plt.imshow(hought)
# plt.show()

# # hought = cv2.resize(hought, (0,0), fx=1, fy=1)
# theta = np.linspace(-np.pi, np.pi, hought.shape[1])
# radii = np.linspace(0, rmax, hought.shape[0])
# tt, rr = np.meshgrid(theta, radii)

# print(theta)
# print(radii)
# print(rr.shape, radii.shape)
# print(tt.shape, theta.shape)

# #hought = cv2.filter2D(hought, -1, np.ones((5,5))/25)
# hmax = np.max(hought)
# rs = rr[hought>(0.4*hmax)]
# ts = tt[hought>(0.4*hmax)]

# disp = np.zeros((ymax, xmax))

# for r, t in zip(rs, ts):
#   print((r,t))
#   xx1 = (xx*np.cos(t) + yy*np.sin(t))
#   clip = np.logical_and(xx1<r+0.5, xx1>r-0.5)
#   disp[clip] = 1

# plt.imshow(hought)
# plt.show()

# plt.imshow(sobel)
# plt.show()

# plt.imshow(disp)
# plt.show()