import numpy as np
import matplotlib.pyplot as plt

r0 = 22.0
x0 = 73.0
B = 400.0

x1 = np.linspace(100, 400, 1000)
# x2 = np.linspace(40, 120, 1000)

R1 = r0 * np.exp(-B*(1/x0 - 1/x1))
# R2 = r0 * np.exp(-B*(1/x0 - 1/x2))


rr = 1000000000000000000000
R1 = 1/(1/rr + 1/R1) 

for i in range(1):

	r = 0.6
	# x2 = np.linspace(100, 10000, 1000)
	V = ( r/(r+R1)) * 1024 *4.5/3.3

	# print(R[999])

	# plt.plot(x1, R)
	# plt.show()

	plt.ylim((0,1024))


	plt.plot(x1, V)
	plt.show()

	# print("R: ",r, "   ,", (-V[:-2] + V[2:])[-1])
	# plt.plot(x1[1:-1], -V[:-2] + V[2:])

plt.show()

# temp = [47, 116, 73, 96, 80]
# otpor = [900, 8.8, 22, 11, 70]

# plt.semilogy(temp, otpor, 'ro')
# plt.semilogy(x2, R2)

# plt.show()