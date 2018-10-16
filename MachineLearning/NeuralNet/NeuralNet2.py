import numpy as np
relu = lambda x: np.maximum(0,x)
step = lambda x: x>0
sigmoid = lambda x: 1 / (1 + np.exp(-x))
dsigmoid = lambda x: sigmoid(x) * (1 - sigmoid(x))

def logCost(neurons, result, M):
	neurons[neurons > 0.9999999] = 0.9999999
	neurons[neurons < 0.0000001] = 0.0000001

	out = -result*np.log(neurons)/M - (1-result)*np.log(1-neurons)/M
	return np.sum(out)

def randomInit(arh):
	ws, bs=[],[]
	for i in range(1,len(arh)):
		bs.append(np.random.randn(arh[i],1))
		ws.append(np.random.randn(arh[i-1], arh[i]).T)
	return ws, bs

# Creating neural network by hand
def forwardProp(X, Ws, bs, funs):
	if (Ws == []) or (bs ==[]) or (funs == []):
		return []
	Z = Ws[0].dot(X) + bs[0]
	A = funs[0](Z)
	return [(Z, A)] + forwardProp(A, Ws[1:], bs[1:], funs[1:])

def BackProp(As, Zs, Ws, bs, grads, D, hparameters):
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
	
	D = Wl.T.dot(D) * grads[0](Zl)

	return [(W, b)] + BackProp(As, Zs, Ws, bs, grads, D, hparameters)

def train(niter, trainData, Ws, bs, funs, grads, hparameters, callback=lambda *x: x):
	if niter <= 0:
		return Ws, bs
	X, Y = trainData
	Zs, As = zip(*forwardProp(X, Ws, bs, funs))
	Zs, As = map(list, (Zs, As))

	A = As.pop()
	Z = Zs.pop()
	D = A - Y

	Ws, bs = zip(*BackProp([X]+As, [None] + Zs, Ws, bs, grads, D, hparameters))
	Ws, bs = map(lambda x: list(reversed(x)), (Ws, bs))

	callback(As+[A], Zs+[Z], Ws, bs)

	return train(niter-1, trainData, Ws, bs, funs, grads, hparameters, callback)


if __name__ == "__main__":
	# Test on xor
	arh = [2, 5, 1]
	trainData = (np.array([[0,0], [0,1], [1,1], [1,0]]).T, np.array([0,1,1,0]))
	Ws, bs = randomInit(arh)
	funs, grads = [relu, sigmoid], [step]
	hparameters = {"alpha": 1}
	nIter = 100

	train(nIter, trainData, Ws, bs, funs=funs, grads=grads, hparameters = hparameters, callback=lambda *x: print(logCost(x[0].pop(), trainData[1], 4)))
