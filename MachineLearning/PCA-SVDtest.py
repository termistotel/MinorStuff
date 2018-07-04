import numpy as np
import cv2
import matplotlib.pyplot as plt

def svdecomposition(mat):
    n,m = mat.shape
    manja = min(n,m)

    sig1, U = np.linalg.eig(mat.dot(mat.T))
    sig2, V = np.linalg.eig(mat.T.dot(mat))

    array1 = np.argsort(sig1)[::-1]
    array2 = np.argsort(sig2)[::-1]

    sig1, U = sig1[array1], U[:,array1]
    sig2, V = sig2[array2], V[:,array2]

    sigma = np.zeros(shape=mat.shape)
    sigma[:manja, :manja] = np.sqrt(np.diag(sig1)[:manja, :manja])
    
    # Fixanje negativnih
    krive = np.diagonal(mat.dot(V).T.dot(U.dot(sigma))) < 0
    V[:,krive] *= -1

    return U, sigma, V

def toGray(P):
	#print P.dtype
	return np.sum(P/(3.0*255), axis=2, dtype="float64")


img = cv2.imread('../res/black_cat.jpg')
img = toGray(img)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# U, s, V = svdecomposition(img)
U, s, V = np.linalg.svd(img)

V = V.T

sigme = s
sigme = sigme[sigme>0.1]
# sigme = sigme[0:1]

U = U[:, :sigme.shape[0]]
V = V[:, :sigme.shape[0]]
rekonstrukcija = U.dot(np.diag(sigme)).dot(V.T)
rekonstrukcija = U.dot(V.T)
# cv2.imshow('img', img)
# cv2.waitKey(0)

cv2.imwrite("testica.png", np.abs(rekonstrukcija))

# for i in range(sigme.shape[0]):
# 	rekonstrukcija = U[:, i:i+1].dot(np.diag(sigme[i:i+1])).dot(V.T[i:i+1, :])
# 	cv2.imshow('img', np.abs(rekonstrukcija))
# 	cv2.waitKey(0)

# plt.loglog(sigme)
# plt.savefig("test.png", bbox_inches='tight')
# plt.show()

plt.rc('text', usetex=True)
fig = plt.figure()
fig, axes = plt.subplots(1,2)
fig.set_figheight(5)
fig.set_figwidth(12)
fig.set_dpi(100)
fig.suptitle("Singular Values")

axes[0].plot(sigme)
axes[0].set_title("Normalan graf")

axes[1].loglog(sigme, 'r')
axes[1].set_title("log-log graf")

for i in axes:
	i.set_xlabel("n", fontsize=20)
	i.set_ylabel('$\sigma$', fontsize=20)

fig.savefig("test.png", bbox_inches='tight')

fig.show()
plt.show()
print(sigme.shape)