import numpy as np
import timy
import cProfile


# reference time 0.000100
@timy.timer(ident='EvA', loops=500)
def EvA(in_array, shape):
    """
    input(list,tuple) -> float
    
    [Ev]aluation [A]lgorithm for Common-Centroid arrangements.
    Function returns Total Mismatch Offset Coefficient (TMOC).
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
    center_of_array = [shape[0] // 2, shape[1] // 2]

    # dictionary for center coordinates for each group
    com_cent = {}

    # find all coordinates for the each group
    for unique_group in unique_groups:
        # write all coordinates for a group number i
        coords = np.argwhere(in_array == unique_group)
        # check if we have more than one element in a group
        if len(coords) > 1:
            # find center of the group
            center_of_group = (np.amin(coords, axis=0) + np.amax(coords, axis=0)) / 2
            com_cent[unique_group] = np.array(center_of_group).tolist()
        else:  # if we have singe element in a group, the algorithm taking it as a center
            com_cent[unique_group] = coords[0].tolist()
        # find difference between center of the groups and the real center of the array
        com_cent[unique_group] = list(np.subtract(com_cent[unique_group], center_of_array))

        TotalMisOffsCoefficient = 0
    # calculation of the TotalMisOffsCoefficient
    for ii, jj in com_cent.values():
        TotalMisOffsCoefficient += abs(ii) + abs(jj)
    return TotalMisOffsCoefficient

# test case
L = [2,3,2,3,1,3,2,3,2]
#L = [1,1,1,1]
#L = []
print(EvA(L,(3,3)))

#cProfile.run('EvA(L,(3,3))')