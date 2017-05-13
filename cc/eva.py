import numpy as np
import timy
import cProfile
import unittest

# reference time 0.000100
#@timy.timer(ident='EvA', loops=500)
def EvA(in_array: object, shape: object) -> object:
    """
    input(list,tuple) -> float
    
    [Ev]aluation [A]lgorithm for Common-Centroid arrangements.
    Function returns Total Mismatch Offset Coefficient (TMOC).
    shape  = (col, rows)
    """

    # base cases if all elements are from the same group return 0
    if len(in_array) == 0:
        print("An input array for the EvA function has no elements.")
        input()  # To let the user see the error message
        import sys
        sys.exit(1)

    # TODO add all the same check
    # if in_array.count(in_array[0]) == len(in_array):
    #     return 0.0

    # convert a list to np.array
    in_array = np.array(in_array)
    # reshape the input array according to the input shape
    in_array = in_array.reshape(shape)

    # find a center of the input array
    center_of_array = [shape[0]/2 -.5,shape[1]/2 -.5]

    # find unique group names (numbers)
    unique_groups, counts = np.unique(in_array, return_counts=True)

    # dictionary for center coordinates for each group
    new_com_cent = {}
    # find all coordinates for the each group
    for i in range(len(unique_groups)):
        new_com_cent[unique_groups[i]] = (sum(np.argwhere(in_array == unique_groups[i])) / counts[i])
        new_com_cent[unique_groups[i]] = list(np.subtract(new_com_cent[unique_groups[i]], center_of_array))

    # calculation of the TotalMisOffsCoefficient (norm 1)
    #print(new_com_cent)
    tmoc = 0
    for ii, jj in new_com_cent.values():
        tmoc += abs(ii) + abs(jj)
    return tmoc.round(True)

# TODO optimize performance
#cProfile.run('EvA(L,(3,3))')

# test case
if __name__ == '__main__':

    class Test_EvA(unittest.TestCase):

        def test_EvA(self):

            L1 = [2, 3, 2, 3, 1, 3, 2, 3, 2]
            self.assertEqual(EvA(L1,(3,3)), 0.0)

            L2 = [1,1,1,1]
            self.assertEqual(EvA(L2,(2,2)), 0.0)

            L3 = [0,1,1,0]
            self.assertEqual(EvA(L3,(2,2)), 0.0)

            L4 = [1,2,1,3,3,3,2,1,2]
            self.assertEqual(EvA(L4,(3,3)), 0.7)

            L5 = [0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]
            self.assertEqual(EvA(L5,(4,4)), 0.0)

            L6 = [2, 3, 2, 3, 1, 3, 2, 3, 2]
            self.assertEqual(EvA(L6, (3, 3)), 0.0)

            L7 = [1,2,1,1]
            self.assertEqual(EvA(L7,(2,2)), 1.3)

            L8 = [1,2,2,1]
            self.assertEqual(EvA(L8,(2,2)), 0.0)

            L9 = [7,5,6,7,
                  4,1,2,3,
                  3,2,1,4,
                  7,6,5,7]

            self.assertEqual(EvA(L9,(4,4)), 0.0)
    unittest.main()