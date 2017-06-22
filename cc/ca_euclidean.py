import numpy as np


def sortRadially(a):
    '''
    lisr -> list
    
    :param a: input_array
    :return: 
    '''
    X, Y = np.indices(a.shape, dtype="float")
    c = int(a.shape[0] / 2)
    d = np.sqrt((c - X) ** 2 + (c - Y) ** 2)
    fd = d.flatten()
    fX = X.flatten()
    fY = Y.flatten()
    argD = fd.argsort()
    nX = fX[argD].astype(int)
    nY = fY[argD].astype(int)
    fa = a.flatten()
    fa.sort()
    for i in range(nX.shape[0]):
        a[nX[i], nY[i]] = fa[i]
    return a


a = np.array([[ 1,  2,  1,],
              [ 1,  3,  3,],
              [ 1,  3,  1,]])

myown = np.random.randint(0, 100, (9, 9))

print("test1:")
print(sortRadially(a))
print("")
print("test2:")
print(sortRadially(myown))