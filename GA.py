import datetime
import numpy as np
from eva import EvA
from random import randint
import timy

# test target, remove it for the real work
target = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# timy decorator for time measurement
@timy.timer(ident='GA_CC_fun')
def GA_CC_fun(target, shape):
    '''
    (list, tuple) -> list
    
    Generic Algorithm for the Common-Centroid optimization 
    
    :param target: a list
    :param shape: a tuple or a list with shape 
    :return: a list
    '''

    def get_fitness(guess, shape):
        '''
        :param guess: 
        :param shape: 
        :return: 
        '''

        return (EvA(np.array(guess), shape))

    def mutate(parent):
        '''
        
        :param parent: 
        :return: 
        '''
        first = randint(0, len(parent) - 1)
        second = randint(0, len(parent) - 1)
        while first == second:
            second = randint(0, len(parent) - 1)
        parent[first], parent[second] = parent[second], parent[first]
        return parent

    def display(guess):
        '''
        
        :param guess: 
        :return: 
        '''
        timeDiff = datetime.datetime.now() - startTime
        fitness = get_fitness(guess, shape)
        print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

    startTime = datetime.datetime.now()

    # best Parent is a target in the beginning
    bestparent = target

    # check initial TMO coefficient
    bestFitness = EvA(np.array(target), shape)

    print("Array \t\t\t\t\t\t\t\t\t\t\t Offset \t time")

    display(bestparent)

    numberofgenerations = 0

    # create a stop criteria
    number_of_irr = 0

    # TODO optimize bellow
    while True and number_of_irr != 40000:
        number_of_irr += 1
        child = mutate(bestparent)
        numberofgenerations += 1
        childFitness = get_fitness(child, shape)
        if bestFitness <= childFitness:
            continue
        display(child)
        if childFitness < 1:
            break
        bestFitness = childFitness
        bestparent = child

    print("Number of generations:", numberofgenerations)

    bestparent = np.array(bestparent)

    return bestparent


print(GA_CC_fun(target, (3, 3)))
