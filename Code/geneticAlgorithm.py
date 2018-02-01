#TODO: create a class for the individual and for the methods that it needs (getters/setters, objective value, etc)
#Abstract the various stages and make sure
#Create classes for each instance of the stages including initalising values such as mutation rate
#Look into python properties for getters and setters and private variables, that is actually pretty cool :)
#Look at the difference between str and repr

#IMPORTS
import random

import constants
from sumSquares import sumSquares

#Set up
random.seed()
problem = sumSquares()

#Initialise and evaluate population
population = []
fitness = []
for i in range(0, constants.POPULATION_SIZE):
    population.append(problem.initialiseIndividual())
    fitness.append(problem.objectiveValue(population[i]))

#Termination Criteria loop, runs for a set number of generations
for x in range(0, constants.NUMBER_OF_GENERATIONS):
    #Main GA loop
    #Set Up
    children = []
    childrenFitness = []
    for i in range(0, constants.POPULATION_SIZE//2):
        #Selection Criteria for parents
        #Currently just random for simplictity
        indexParent1 = problem.selection(constants.POPULATION_SIZE)
        indexParent2 = problem.selection(constants.POPULATION_SIZE)

        #Apply Crossover to generate offspring
        children.append(problem.crossover(population[indexParent1], population[indexParent2]))

        #Apply Mutation
        children[i] = problem.mutation(children[i], constants.MUTATION_RATE)

        #Validation
        children[i] = problem.validation(children[i])

        #Evaluate fitness
        childrenFitness.append(problem.objectiveValue(children[i]))

    #Population Replacement
    for i in range(0, len(children)):
        population, fitness = problem.populationReplacement(population, fitness, children[i], childrenFitness[i], constants.POPULATION_SIZE)

    #Print out the population
    print('\n Generation ' + str(x))
    for i in range(0, len(population)):
        print(population[i])


#print out the best value
bestIndex = 0
bestFitness = fitness[bestIndex]
for i in range(1, constants.POPULATION_SIZE):
    if( fitness[i] < bestFitness ):
        bestIndex = i
        bestFitness = fitness[i]
print('\n Best Result')
print(population[bestIndex])
print(bestFitness)
