from cc.ca_sym import construction_algorithm_symmetry
from cc.eva import EvA
from cc.ga import ga_cc
import numpy as np

def cc_main_flow(input_list, square_array, orientation = "ver", num_dummy_rows = 0, row_numbers = 0):
    '''
    (list, bool, str, int, int) -> list 
    
    :param in_device_list: list, input number of devices e.g. [1,2,3] == [1A, 2B, 3C]
    :param square_array: boolean 
    :param orientation: "ver" or "hor", ignored when square_array == True
    :param num_dummy_rows: int 
    :param row_numbers: int 
    :return: list
    '''

    ouput_from_ca = np.array(construction_algorithm_symmetry(input_list, square_array,
                                                    orientation, num_dummy_rows = 0, row_numbers = 0))
    if EvA(ouput_from_ca, ouput_from_ca.shape) != 0.0:
        return ga_cc(ouput_from_ca, ouput_from_ca.shape)
    else:
        print("ELSE:")
        return ouput_from_ca




print(cc_main_flow([1,2], True))