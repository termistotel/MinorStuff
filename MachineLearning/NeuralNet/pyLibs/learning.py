import numpy as np
from pyLibs.forwardProp import simpleForwardProp
from pyLibs.backProp import numericBackProp

def simpleTrain(niter, trainData, forwardprop, backprop, Ws, bs, funs, grads, cost, hparameters, callback=lambda *x: x, numericCompare=False):
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

	# Calculate numeric gradients for debug
	if numericCompare:
		dWs1, dbs1 = numericBackProp(X, Y, Ws, bs, funs, cost, forwardprop, epsilon = 0.0001)

	# Perform backpropagation
	Ws, bs, gradsW, gradsb = zip(*backprop([X]+As, [None] + Zs, Ws, bs, funs, grads[:-1], cost, D, hparameters))
	Ws, bs, gradsW, gradsb = map(lambda x: list(x), (Ws, bs, gradsW, gradsb))

	# Print numeric gradient for debuging purpose
	if numericCompare:
		for dW1, dW in zip(dWs1, gradsW):
			print("numeric gradient difference W: ")
			diff = dW1-dW
			print(diff[diff>0.000001])
		for db1, db in zip(dbs1, gradsb):
			print("numeric gradient difference b: ")
			diff = db1-db
			print(diff[diff>0.000001])

	callback(As+[A], Zs+[Z], Ws, bs)

	return simpleTrain(niter-1, trainData, forwardprop, backprop, Ws, bs, funs, grads, cost, hparameters, callback = callback, numericCompare = numericCompare)
