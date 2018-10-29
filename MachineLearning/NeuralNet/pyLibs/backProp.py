import numpy as np

def simpleBackProp(As, Zs, Ws, bs, grads, D, hparameters):
	if (Ws == []) or (bs ==[]):
		return []

	Wl, bl = Ws.pop(), bs.pop()
	Zl, Al = Zs.pop(), As.pop()
	lrate = hparameters["alpha"]
	M = Al.shape[0]

	W = Wl - lrate/M * D.dot(Al.T)
	b = bl - lrate/M * np.sum(D, axis=1, keepdims=True)

	# print(b.shape, bl.shape, D.shape, np.sum(D, axis=1, keepdims=True).shape)

	if Zl is None:
		return [(W, b)]
	
	grad = grads[-1]
	D = Wl.T.dot(D) * grad(Zl)

	return simpleBackProp(As, Zs, Ws, bs, grads[:-1], D, hparameters) + [(W, b)]

def numericBackProp(As, Zs, Ws, bs, grads, D, hparameters):
	pass