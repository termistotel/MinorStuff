import numpy as np
from pyLibs.forwardProp import simpleForwardProp

def simpleTrain(niter, trainData, forwardprop, backprop, Ws, bs, funs, grads, hparameters, callback=lambda *x: x):
	""" train recursively trains

		niter is the number of iterations
		trainData is a touple of X-s and Y-s
		Ws is the list of weights
		bs is the list of bias'
		funs is the list of activation functions for each layer
		hparameters is a dict of hiperparameters

		callback function is a a function that is called every epoch
			it takes argumetns As, Zs, Ws and bs"""

	# Iteration termination condition
	if niter <= 0:
		return Ws, bs

	# Extracting training data
	X, Y = trainData

	# Forward propagation
	Zs, As = zip(*forwardprop(X, Ws, bs, funs))
	Zs, As = map(list, (Zs, As))

	# Starting iteration:
	# D = (dj/dZ)(Z) * (dAL/dZ)(Z)
	#
	# For a good choice of cost function and final layer actiation:
	# D = A - Y
	A = As.pop()
	Z = Zs.pop()
	grad = grads[-1]
	D = A - Y

	Ws, bs = zip(*backprop([X]+As, [None] + Zs, Ws, bs, grads[:-1], D, hparameters))
	Ws, bs = map(lambda x: list(x), (Ws, bs))

	callback(As+[A], Zs+[Z], Ws, bs)

	return simpleTrain(niter-1, trainData, forwardprop, backprop, Ws, bs, funs, grads, hparameters, callback)
