import numpy as np
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap

@timing
def conv1(A, W, final, cache):
  f, nh1, nw1 = cache['f'], cache['nh1'], cache['nw1']
  for i in range(f):
    for j in range(f):
      final += np.sum(A[:, i:i+nh1, j:j+nw1,:,:]*W[i, j, :, :], axis=3)
  print(final[0,:2,:2,2])

@timing
def conv2(A, W, final, cache):
  f, nh1, nw1 = cache['f'], cache['nh1'], cache['nw1']
  for x in range(nh1):
    for y in range(nw1):
      part = A[:, x:x+f, y:y+f, :, :]
      final[:, x, y, :] = np.sum(part*W, axis=(1,2,3))
  print(A[0, 2:4, 2:4, 1, 0])
  print(final[0,:2,:2,1])


p = 0
s = 1
f = 5
nc = 10
nh = 800
nw = 600
m = 30


W1 = np.zeros(shape=(f,f))
W2 = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0]])
W3 = np.zeros(shape=(f,f))

W = np.array([W1, W2, W3])
W = np.array([W for i in range(nc)])
W = W.transpose([2,3,1,0])

A = np.random.rand(m, nh, nw, 3, 1)

nh1, nw1 = int((nh + 2*p - f)/s + 1), int((nw + 2*p - f)/s + 1)

final = np.zeros(shape=(m,nh1,nw1,nc))
cache = {'p':p, 's':s, 'f':f, 'nc':nc, 'nh':nh, 'nw':nw, 'm':m, 'nh1':nh1, 'nw1':nw1}

# conv2(A, W, final, cache)

for i in range(10):
#   final = np.zeros(shape=(m,nh1,nw1,nc))
#   conv1(A, W, final, cache)
  final = np.zeros(shape=(m,nh1,nw1,nc))
  conv2(A, W, final, cache)
