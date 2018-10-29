import numpy as np
from pyLibs.randomInit import simpleRandomInit
from pyLibs.forwardProp import simpleForwardProp
from pyLibs.backProp import simpleBackProp
from pyLibs.learning import simpleTrain

import pyLibs.getData as data
import pyLibs.mathFuns as m

from functools import partial

def callback(Ys, As, Zs, Ws, bs):
	print(m.logCost(As[-1], Ys, Ys.shape[0]), As[-1], Ys)

if __name__ == "__main__":
	# Test on xor
	trainData = data.getXor()

	arh = [trainData[0].shape[0]] + [10, 1]

	# Neural net initialization
	nIter = 5
	forwardprop = simpleForwardProp
	backprop = simpleBackProp
	Ws, bs = simpleRandomInit(arh)
	funs, grads = [m.relu, m.sigmoid], [m.step, m.dsigmoid]
	hparameters = {"alpha": 2}
	cost = m.logCost

	simpleTrain(nIter, trainData, forwardprop, backprop, Ws, bs, funs=funs, grads=grads, cost=cost, hparameters = hparameters, callback=partial(callback, trainData[1]), numericCompare=True)
