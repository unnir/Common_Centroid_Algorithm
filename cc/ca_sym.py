import math
from itertools import zip_longest

# test packs
import unittest
import timy

#@timy.timer(ident='construction_algorithm_symmetry', loops=500) # ref time 0,000043
def construction_algorithm_symmetry(in_device_list, square_array = True, orientation = 'ver', num_dummy_rows = 0, row_numbers = 0):
    '''
    (list, bool, str, int, int) -> list 
    
    A constructive algorithm, for an initial close to optimum solution. 
    
    :param in_device_list: list, input number of devices e.g. [1,2,3] == [1A, 2B, 3C]
    :param square_array: boolean 
    :param orientation: "ver" or "hor", ignored when square_array == True
    :param num_dummy_rows: int 
    :param row_numbers: int 
    :return: list
    '''


    # TODO add possibility of shape control
    if num_dummy_rows == 0:
        pass
    else:
        nnn = num_dummy_rows

    def make_rows(L, Col):
        '''
        (list, int) -> list
        
        separate the input list L in sub-list
        :param L: list
        :param Col: int
        :return: tuple
        '''
        z = ()
        for i in range(0, len(L), Col):
            z += (L[i:i + Col],)
        return z

    # exchange first and last element. Reason for a better symmetry.
    if len(in_device_list) is 2 and in_device_list[0] < in_device_list[1]:
        in_device_list[0], in_device_list[1] = in_device_list[1], in_device_list[0]


    '''
    Converting the in_device_list to the working_list.
    E.g. [1,2,3] or [1A, 2B, 3C] to [1, 2, 2, 3, 3, 3] 
    which is [A1, B1, B2, C1, C2, C3]
    '''
    if square_array is False:
        new_list = {}
        cnt = 0
        group_cnt = -1
        for group in in_device_list:
            cnt += 1
            group_cnt += 1
            new_list[group_cnt] = ()
            for y in range(group):
                new_list[group_cnt] += (cnt,)
        sorted_matrix = new_list.values()

    elif square_array is True:

        cnt = 0
        working_list = []
        for group in in_device_list:
            cnt += 1
            for y in range(group):
                working_list += [cnt, ]

        # sorted_matrix = working_list
        temp_list = working_list
        sqrt = int(math.ceil(math.sqrt(len(temp_list))))
        for iDummy in range(sqrt * sqrt - len(temp_list)):
            temp_list += (0,)
        new_tuple = make_rows(temp_list, sqrt)
        sorted_matrix = new_tuple

    # transpose the working array
    transposed_array = [[e for e in li if e is not None] for li in zip_longest(*sorted_matrix)]

    # create a dict for rows
    rows = {}

    for row_number, i_rows in enumerate(transposed_array):
        # divide the row into two list right and left, selected each second element Fig. 2 (b) and (c)
        right = i_rows[::2]
        left = i_rows[1::2]

        if square_array is False:
            if len(left) < len(in_device_list) / 2:
                for i in range(int(len(in_device_list) / 2 - len(left))):
                    left.append(0)
            if len(right) < len(in_device_list) / 2:
                for i in range(int(len(in_device_list) / 2 - len(right))):
                    right.append(0)
        # for the better symmetry
        left = list(reversed(left))
        if (len(in_device_list) % 2 != 0) and ((row_number % 2) == 0):
                right[0], left[-1] = left[-1], right[0]

        rows[row_number] = left + right

        if square_array is False and (len(in_device_list) != len(i_rows)):
                rows[row_number].append(0)
        # if a dummy inside
        if (row_number % 2) == 0:
            rows[row_number] = list(reversed(i_rows))




    final_matrix = list(rows.values())
    # for i in range(len(final_matrix)):
    #     if 1 in final_matrix[i]:
    #         marker = i


    # exchange first and last row, for a better symmetry
    if final_matrix[0] != final_matrix[len(final_matrix) - 1]:
        final_matrix.insert(0, final_matrix.pop(len(final_matrix) - 1))

    rotated = [[e for e in li if e is not None] for li in zip_longest(*final_matrix)]

    # check if row numbers is 0, it means a user hasn't define the row/col parameters
    if row_numbers is 0:
        if orientation == "hor":
            if len(rotated[0]) > len(final_matrix[0]):
                return rotated
            else:
                return final_matrix
        elif orientation == "vert":
            if len(rotated) > len(final_matrix):
                return rotated
            else:
                return final_matrix
        else:
            return final_matrix

        return final_matrix
    else:
        # base case if the wanted row number is 1
        if row_numbers is 1:
            # return a flat list
            return sum(rotated, [])
        elif len(rotated) is not row_numbers:
            # flat the list
            rotated = sum(rotated, [])
            tot_number_of_elemetns = len(rotated)
            if tot_number_of_elemetns % row_numbers is not 0:
                # add dummy elements
                old_len = len(rotated)
                [rotated.append(0) for i in range(row_numbers - old_len % row_numbers)]

                rotated = list(make_rows(rotated, int(len(rotated) / row_numbers)))
                return rotated
            else:
                # make a new
                return make_rows(rotated, tot_number_of_elemetns / row_numbers)
        else:
            return rotated



if __name__ == '__main__':

    class Test_construction_algorithm_symmetry(unittest.TestCase):
        def test_construction_algorithm_symmetry(self):
            self.assertEqual(construction_algorithm_symmetry([1, 1, 1, 1, 1, 1, 1, 1, 1], square_array=True, orientation="ver"),
                             [[9, 6, 3],
                              [7, 4, 1],
                              [5, 2, 8]])

            self.assertEqual(construction_algorithm_symmetry([2, 4, 8, 16], square_array=True, orientation="ver"),
                             [[0, 4, 3, 2, 4, 4],
                              [0, 4, 4, 3, 3, 1],
                              [0, 4, 3, 1, 3, 4],
                              [0, 4, 4, 4, 3, 2],
                              [0, 4, 3, 2, 4, 4],
                              [0, 4, 4, 4, 3, 2]])

            self.assertEqual(construction_algorithm_symmetry([2, 4, 8, 16], square_array=True, orientation="ver"),
                             [[0, 4, 3, 2, 4, 4],
                              [0, 4, 4, 3, 3, 1],
                              [0, 4, 3, 1, 3, 4],
                              [0, 4, 4, 4, 3, 2],
                              [0, 4, 3, 2, 4, 4],
                              [0, 4, 4, 4, 3, 2]])

            self.assertEqual(construction_algorithm_symmetry([3,3,3], row_numbers = 3),
                            [[3, 2, 3],
                             [2, 1, 2],
                             [1, 3, 1]])


            self.assertEqual(construction_algorithm_symmetry([3,3,3], row_numbers = 4),
                            [[3, 2, 3],
                             [2, 1, 2],
                             [1, 3, 1],
                             [0, 0, 0]])

            self.assertEqual(construction_algorithm_symmetry([3,3,3], row_numbers = 1),
                            [3, 2, 3, 2, 1, 2, 1, 3, 1])
    unittest.main()