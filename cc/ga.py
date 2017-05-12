import datetime
from random import randint
import numpy as np
from cc.eva import EvA

import timy
import unittest

# test target, remove it for the real work
target = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# timy decorator for time measurement
#@timy.timer(ident='ga_cc')
def ga_cc(target, shape):
    '''
    (list, tuple) -> list
    
    Generic Algorithm for the Common-Centroid optimization 
    
    :param target: a list
    :param shape: a tuple or a list with shape 
    :return: a list
    '''

    def get_fitness(guess, shape):
        '''
        (list, list) -> float
        
        :param guess:  list
        :param shape:  tuple or list
        :return: float 
        '''

        return (EvA(np.array(guess), shape))

    def mutate(parent):
        '''
        (list) -> list
        
        :param parent: list 
        :return: list
        '''
        first = randint(0, len(parent) - 1)
        second = randint(0, len(parent) - 1)
        while first == second:
            second = randint(0, len(parent) - 1)
        parent[first], parent[second] = parent[second], parent[first]
        return parent

    def display(guess):
        '''
        (list) -> print function 
        
        :param guess: list
        :return: print function 
        '''
        timeDiff = datetime.datetime.now() - startTime
        fitness = get_fitness(guess, shape)
        print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

    # start the clock times
    startTime = datetime.datetime.now()

    # best Parent is a target in the beginning
    bestparent = target

    # check initial TMO coefficient
    bestFitness = EvA(np.array(target), shape)

    # print head for the
    print("Array \t\t\t\t\t\t\t\t\t\t\t Offset \t time")

    # display the first result
    display(bestparent)

    # set up number of generations
    numberofgenerations = 0

    # create a stop criteria
    number_of_irr = 0

    # create min wanted TMO coefficient
    wanted_tmoc = 0.5
    # TODO optimize bellow
    while number_of_irr != 1000000:
        number_of_irr += 1
        child = mutate(bestparent)

        numberofgenerations += 1
        childFitness = get_fitness(child, shape)

        if bestFitness <= childFitness:
            continue
        display(child)
        if childFitness < wanted_tmoc:
            break
        bestFitness = childFitness
        bestparent = child
    # TODO a new loop with lower wanted TMO coef.
    bestparent = np.array(bestparent)

    return bestparent.tolist()

#print(ga_cc([1,1,2,2,3,3,4,4,5,5,6,6,7,7,7,7],(4,4)))


if __name__ == '__main__':
    class Test_ga_cc(unittest.TestCase):
        def test_ga_cc(self):
            L_in_1 =  [1,1,1,1,1,1,1,1,2]
            L_out_1 = [1,1,1,1,2,1,1,1,1]
            self.assertEqual(ga_cc(L_in_1,(3,3)),L_out_1)
    unittest.main()