import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
from math import pi

def dl(r, fi, z):
	dfi = fi[2:] - fi[:-2]
	dz = z[2:] - z[:-2]
	return np.array([-r[1:-1]*np.sin(fi[1:-1])*dfi, r[1:-1]*np.cos(fi[1:-1])*dfi, dz]).T

def transf(r, fi, z):
	return r* np.cos(fi), r* np.sin(fi), z

def B(x,y,z, I, container, dls):
	r = np.array([[x,y,z]])

	er = container- r
	ernorm = np.array([np.sqrt(np.square(er[:,0]) + np.square(er[:,1]) + np.square(er[:,2]))**3]).T
	kros = I*np.cross(dls, er)

	return np.sum(kros/ernorm, axis=0)

def silnice(n,dx,ax,xmin,xmax,B1):
	for i in np.linspace(xmin, xmax, n):
		polozaj = np.array([i, 0, 0])
		lista = np.array([polozaj])
		for j in range(150):
			be = B1(polozaj)
			be[1] = 0
			polozaj += dx*be / norm(be)
			lista = np.append(lista,[polozaj], axis=0)
			if not polozaj[2]<0:
				break

		polozaj = np.array([i, 0, 0])
		for j in range(150):
			be = B1(polozaj)
			be[1] = 0
			polozaj -= dx*be / norm(be)
			lista = np.append([polozaj],lista, axis=0)
			if not polozaj[2]>0:
				break

	 	ax.plot(lista[:,0],lista[:,1],lista[:,2])

n = 10000
r = 1
h = 1
zmin, zmax = -10,10

phimin = 0
phimax = phimin + (zmax - zmin)/h * 2 *pi

fis = np.linspace(phimin, phimax, n)
zs = np.linspace(zmin, zmax, n)
#fis = np.linspace(0, 2*pi, n)
#zs = np.zeros(n)
rs = r*np.ones(n)

xs,ys,zs = transf(rs,fis,zs)

container = np.zeros(shape=(n-2,3))
container[:,0] = xs[1:-1]
container[:,1] = ys[1:-1]
container[:,2] = zs[1:-1]
I = 2
dls = dl(rs,fis,zs)

B1 = lambda point: B(point[0],point[1],point[2],I, container, dls)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlim3d(-2,2)
ax.set_ylim3d(-2,2)
ax.set_zlim3d(-10,10)

ax.plot(xs, ys, zs)

silnice(10,0.1,ax,-0.8*r, 0.8*r, B1)

plt.show()