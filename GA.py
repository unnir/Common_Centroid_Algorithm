import datetime
import random
import numpy as np
from eva import EvA
from random import randint

# test target
target = [1, 1, 1, 2, 2, 2, 3, 3, 3]


def GA_CC_fun(target, shape_):
    def generate_parent(length):
        random.shuffle(length, random.random)
        return length

    def get_fitness(guess, shape_):

        return (EvA(np.array(guess), shape_))

    def mutate(parent):
        first = randint(0, len(parent) - 1)
        second = randint(0, len(parent) - 1)
        while first == second:
            second = randint(0, len(parent) - 1)
        parent[first], parent[second] = parent[second], parent[first]
        return parent

    def display(guess):
        timeDiff = datetime.datetime.now() - startTime
        fitness = get_fitness(guess, shape_)
        print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

    startTime = datetime.datetime.now()

    bestParent = generate_parent(target)
    bestFitness = 10
    print("Array \t\t\t\t\t\t\t\t\t\t\t Offset \t time")

    display(bestParent)

    NNN = 0
    NumberOfIrr = 0

    # TODO optimize bellow
    while True and NumberOfIrr != 40000:
        NumberOfIrr += 1
        child = mutate(bestParent)
        NNN += 1
        # print("child",child)
        childFitness = get_fitness(child, shape_)
        if bestFitness <= childFitness:
            continue
        display(child)
        if childFitness < 1:
            break
        bestFitness = childFitness
        bestParent = child

    print("Number of generations:", NNN)

    bestParent = np.array(bestParent)

    return bestParent


print(GA_CC_fun(target, (3, 3)))
