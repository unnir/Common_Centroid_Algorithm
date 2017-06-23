import numpy as np
import unittest


# TODO add shape param to the function
def construction_algorithm_euclidean(input_array):
    '''
    list -> list
    
    :param input_array: input_array
    :param shape: tuple, list (n,m)
    :return: list
    '''
    input_array = np.array(input_array)

    X, Y = np.indices(input_array.shape, dtype="float")

    c = int(input_array.shape[0] / 2)
    # calculate distance to each position in the array
    d = np.sqrt((c - X) ** 2 + (c - Y) ** 2)
    # flat the distance marks
    fd = d.flatten()
    # flat the coordinates
    fX = X.flatten()
    fY = Y.flatten()
    # indicates the smallest element in fd
    argD = fd.argsort()
    nX = fX[argD].astype(int)
    nY = fY[argD].astype(int)
    fa = input_array.flatten()
    fa.sort()
    for i in range(len(nX)):
        input_array[nX[i], nY[i]] = fa[i]
    return input_array.tolist()


a = np.array([[ 1,  2,  1],
              [ 1,  3,  3],
              [ 1,  3,  1]])



if __name__ == '__main__':

    class Test_construction_algorithm_euclidean(unittest.TestCase):
        def test_construction_algorithm_euclidean(self):
            self.assertEqual(construction_algorithm_euclidean([[ 1,  2,  1,],[ 1,  3,  3,],[ 1,  3,  1,]]),
                             [[2, 1, 3],
                              [1, 1, 1],
                             [3, 1, 3]])

    unittest.main()