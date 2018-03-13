import numpy as np
import matplotlib.pyplot as plt

# beta = 1
# R = 1000000.0
# R1 = beta*R
# Rref = 100000.0

# def ruk(r):
# 	return R-R1*R1/(R1+r)

# def dc(r):
# 	return (ruk(r) + Rref)/(2*ruk(r) + Rref)

# r = np.logspace(2, 9, 1000)

# for R1 in np.linspace(1000, 100000, 10):
# 	plt.semilogx(r, dc(r))
# plt.show()

# for beta in np.linspace(0,1, 10):
# 	R1 = beta*R
# 	for Rref in np.linspace(1000, 1000000, 10):
# 		plt.semilogx(r, dc(r))

# 	print(beta)
# 	plt.show()

# alfa = 10
# beta = alfa

# konst = 10

# x = np.logspace(-3,3,100)

# def dc(x):
# 	return 1.0-1.0/(2+1/(alfa-beta*beta/(beta+x)))

# for alfa in np.linspace(0.1,10,3):
# 	for beta in np.linspace(0,alfa,3):
# 	#beta = alfa
# 		plt.semilogx(x,dc(x))
# plt.show()


R0 = 2000000
def dc1(g, Rref, R):
	x = Rref/(1*R0* np.exp(-2*g))
	x0 = Rref/R
	return 1-1.0/(2+ (x+x0))

def dc(g, Rref, R):
	x = (R0* np.exp(-g))
	return 1.0/(2 + x/Rref)

G = np.linspace(0, 10, 1000)

Rref = 100000
R = 1000000000000

for Rref in np.linspace(100, 100000, 10):
	plt.plot(G, dc(G, Rref, R))


plt.show()