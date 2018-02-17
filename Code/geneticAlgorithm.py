#TODO: create a class for the individual and for the methods that it needs (getters/setters, objective value, etc)
#Abstract the various stages and make sure
#Create classes for each instance of the stages including initalising values such as mutation rate
#Look into python properties for getters and setters and private variables, that is actually pretty cool :)
#Look at the difference between str and repr

#TODO: AT ANY POINT THERE COULD BE TOO MANY REQUESTS ??? WHAT DO

#IMPORTS
import random

import constants
from proofOfConcept.sumSquares import sumSquares
from pokemonTeamProblem import pokemonTeamProblem

#Set up
random.seed(1522018)
problem = pokemonTeamProblem()

#Print out the parameters
print("-------------------- Global  Parameters --------------------")
print("Number of Generations = " + str(constants.NUMBER_OF_GENERATIONS))
print("Population Size       = " + str(constants.POPULATION_SIZE))
print("Mutation Rate         = " + str(constants.MUTATION_RATE*100) + "%")
print("------------------------------------------------------------" + "\n")

#Initialise population
print("----------------- Initialising  Population -----------------")
population = []
for i in range(0, constants.POPULATION_SIZE):
    population.append(problem.initialiseIndividual())
    print("Generated Individual")
    print(population[i])
#Evaluate population
fitness = []
for i in range(0, constants.POPULATION_SIZE):
    problem.objectiveValuePop(population[i], population)
    print("Evaulated individual")

#Termination Criteria loop, runs for a set number of generations
for x in range(0, constants.NUMBER_OF_GENERATIONS):
    #Main GA loop
    #Set Up
    children = []
    childrenFitness = []
    for i in range(0, constants.POPULATION_SIZE//2):
        #Selection Criteria for parents
        indexParent1 = problem.selection(constants.POPULATION_SIZE)
        indexParent2 = problem.selection(constants.POPULATION_SIZE)
        while indexParent1 == indexParent2:
            indexParent2 = problem.selection(constants.POPULATION_SIZE)

        #Apply Crossover to generate offspring
        children.append(problem.crossover(population[indexParent1], population[indexParent2]))

        #Apply Mutation
        children[i] = problem.mutation(children[i], constants.MUTATION_RATE)

        #Validation
        children[i] = problem.validation(children[i])

        #Evaluate fitness
        #childrenFitness.append(problem.objectiveValuePop(children[i], population))
        ov = problem.objectiveValuePop(children[i], population)
        print(ov)
        childrenFitness.append(ov)

        #childrenFitness.append(problem.objectiveValue(children[i]))

    #Population Replacement
    for i in range(0, len(children)):
        population, fitness = problem.populationReplacement(population, fitness, children[i], childrenFitness[i], constants.POPULATION_SIZE)

    #Print out the population
    print('\n Generation ' + str(x))
    # #Print entire population
    # for i in range(0, len(population)):
    #     print(population[i])


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
