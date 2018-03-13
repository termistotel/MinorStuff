import numpy as np

def numElems(ws):
	n = 0
	for x,y in ws:
		n += x*y
	return n

def forwardProp(X, shapes, weights, biass, funs):
    As = [X]
    Zs = []
    A = X
    nw = 0
    nb = 0

    for fun,shape in zip(funs, shapes):

    	size = shape[0]*shape[1]

    	#Take weights
    	W = weights[nw:size].reshape(shape)
    	nw += size

    	#Take bias'
    	b = biass[nb:shape[0]]
    	nb += broj

        Z = W.dot(A) + b
        A = fun(Z)
        Zs.append(Z)
        As.append(A)

    return As, Zs

def forwardProp(X, weights, biass, funs):
    As = [X]
    Zs = []
    A = X
    for fun,W,b in zip(funs, weights, biass):
        Z = W.dot(A) + b
        A = fun(Z)
        Zs.append(Z)
        As.append(A)
    return As, Zs

nx = 2
ny = 1

nh = [3,5]

n = [nx] + nh + [ny]

wshapes = zip(n[1:], n)
Ws = np.random.randn(numElems(wsizes))
Wss = []
tmp = 0

for shape in wshapes:
	size = shape[0]*shape[1]
	Wss.append(Ws[tmp:size])
