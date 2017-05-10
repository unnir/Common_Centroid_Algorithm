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

    # convert a list to np.array
    in_array = np.array(in_array)
    # reshape the input array according to the input shape
    in_array = in_array.reshape(shape)
    # find unique group names (numbers)
    unique_groups = np.unique(in_array)

    # find real center of the input array in_array
    center_of_array = [(shape[0] / 2 - .5) if (shape[0] % 2 == 0) else shape[0] / 2,
                        shape[1] / 2 - .5 if (shape[1] % 2 == 0) else shape[1] / 2 ]
    # dictionary for center coordinates for each group
    com_cent = {}

    # find all coordinates for the each group
    for unique_group in unique_groups:
        # write all coordinates for a group number i
        coords = np.argwhere(in_array == unique_group)

        # TODO think about a better solution
        bias = np.array([0, 0.0])
        if shape[0] % 2 != 0:
            bias += [0.5, 0]
        if shape[1] % 2 != 0:
            bias += [0, 0.5]
        # check if we have more than one element in a group
        if len(coords) > 1:
            # find center of the group
            center_of_group = (np.amin(coords, axis=0) + np.amax(coords, axis=0)) / 2 + bias
            com_cent[unique_group] = np.array(center_of_group).tolist()
        else:  # if we have singe element in a group, the algorithm taking it as a center
            com_cent[unique_group] = coords[0].tolist() + bias
        # find difference between center of the groups and the real center of the array
        com_cent[unique_group] = list(np.subtract(com_cent[unique_group], center_of_array))
        # TMOC
        tmoc = 0
    # calculation of the TotalMisOffsCoefficient (norm 1)
    for ii, jj in com_cent.values():
        tmoc += abs(ii) + abs(jj)
    return tmoc

# TODO optimize performance
#cProfile.run('EvA(L,(3,3))')

# test case
if __name__ == '__main__':

    class Test_construction_algorithm_symmetry(unittest.TestCase):

        def test_construction_algorithm_symmetry(self):

            L1 = [2, 3, 2, 3, 1, 3, 2, 3, 2]
            self.assertEqual(EvA(L1,(3,3)), 0.0)

            L2 = [1,1,1,1]
            self.assertEqual(EvA(L2,(2,2)), 0.0)

            L3 = [0,1,1,0]
            self.assertEqual(EvA(L3,(2,2)), 0.0)

            L4 = [1,2,1,3,3,3,2,1,2]
            self.assertEqual(EvA(L4,(3,3)), 0.0)

            L5 = [0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]
            self.assertEqual(EvA(L5,(4,4)), 0.0)

            L6 = [2, 3, 2, 3, 1, 3, 2, 3, 2]
            self.assertEqual(EvA(L6, (3, 3)), 0.0)

            L7 = [1,2,1,1]
            self.assertEqual(EvA(L7,(2,2)), 1.0)

    unittest.main()