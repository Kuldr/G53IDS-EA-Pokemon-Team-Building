#IMPORTS
import random

import constants

#Set up
random.seed()

#Initialise and evaluate population
population = []
fitness = []
for i in range(0, constants.POPULATION_SIZE):
    population.append([random.randrange(-5, 5),random.randrange(-5, 5)])
    fitness.append(population[i][0]**2 + population[i][1]**2)
print(population)
print(fitness)

#Termination Criteria loop, runs for a set number of generations
for x in range(0, constants.NUMBER_OF_GENERATIONS):
    #Main GA loop
    #Set Up
    children = []
    childrenFitness = []
    for i in range(0, constants.POPULATION_SIZE/2):
        #Selection Criteria for parents
        #Currently just random for simplictity
        indexParent1 = random.randrange(constants.POPULATION_SIZE)
        indexParent2 = random.randrange(constants.POPULATION_SIZE)

        #Apply Crossover to generate offspring
        children.append([population[indexParent1][0], population[indexParent2][1]])

        #Apply Mutation
        if( random.random() <= constants.MUTATION_RATE ):
            children[i][random.randrange(2)] *= random.uniform(-1.5, 1.5)

        #Validation
        if( children[i][0] > 10 ):
            children[i][0] = 10
        if( children[i][1] > 10 ):
            children[i][1] = 10
        if( children[i][0] < -10 ):
            children[i][0] = -10
        if( children[i][1] < -10 ):
            children[i][1] = -10

        #Evaluate fitness
        childrenFitness.append(children[i][0]**2 + children[i][1]**2)

    #Population Replacement
    for i in range(0, len(children)):
        #Random Replacement
        indexToChange = random.randrange(constants.POPULATION_SIZE)
        population[indexToChange] = children[i]
        fitness[indexToChange] = childrenFitness[i]

print(population)
print(fitness)
