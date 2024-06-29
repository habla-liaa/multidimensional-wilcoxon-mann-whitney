from scipy.spatial.distance import pdist, squareform
import numpy as np

def _multidimensional_ranksum(d, y):
    argsorts = np.argsort(d,axis=0)
    x = y[argsorts]
    m = x[0]==x[1:]
    n1 = np.sum(m,axis=0)
    N = x.shape[1]
    n2 = N-n1
    ix = np.tile(np.arange(1, N).reshape(-1,1),(1,N))
    U1 = np.where(m, ix, np.zeros_like(ix)).sum(0) - n1*(n1+1)/2
    U2 = np.where(~m, ix, np.zeros_like(ix)).sum(0) - n2*(n2+1)/2
    U = np.where(U1>U2, U1, U2)/n1/n2
    return argsorts, U

def multidimensional_ranksum(X, y, distance = "euclidean"):
    d = pdist(X, metric=distance)
    d = squareform(d)
    argsorts, U = _multidimensional_ranksum(d, y)
    return argsorts, U