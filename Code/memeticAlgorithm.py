#TODO: create a class for the individual and for the methods that it needs (getters/setters, objective value, etc)
#Abstract the various stages and make sure
#Create classes for each instance of the stages including initalising values such as mutation rate
#Look into python properties for getters and setters and private variables, that is actually pretty cool :)
#Look at the difference between str and repr

#TODO: AT ANY POINT THERE COULD BE TOO MANY REQUESTS ??? WHAT DO

#IMPORTS
import random
from datetime import datetime

import constants
from proofOfConcept.sumSquares import sumSquares
from pokemonTeamProblem import pokemonTeamProblem

#Set up
random.seed(1522018)
#problem = sumSquares()
problem = pokemonTeamProblem()

#Print out the parameters
print("------------------------- Global  Parameters -------------------------")
print("Number of Generations = " + str(constants.NUMBER_OF_GENERATIONS))
print("Population Size       = " + str(constants.POPULATION_SIZE))
print("Mutation Rate         = " + str(constants.MUTATION_RATE*100) + "%")
print("Local Search Steps    = " + str(constants.LOCAL_SEARCH_STEPS))
print("Start Time            = " + str(datetime.now()))
print("----------------------------------------------------------------------" + "\n")

#Initialise population
print("---------------------- Initialising  Population ----------------------")
population = []
fitness = []
for i in range(0, constants.POPULATION_SIZE):
    print("Generating individual - " + str(i))
    population.append(problem.initialiseIndividual())
print("----------------------------------------------------------------------" + "\n")

#Termination Criteria loop, runs for a set number of generations
for x in range(0, constants.NUMBER_OF_GENERATIONS):
    #Main GA loop
    print("---------------------------- Generation " + str(x) + " ----------------------------")

    #Evaluate population
    print("Evaluating Population")
    fitness = []
    for i in range(0, constants.POPULATION_SIZE):
        print("\tEvaluating individual - " + str(i))
        fitness.append(problem.objectiveValuePop(population[i], population))
        print("\tEvaulated individual Score = " + str(fitness[i]))

    #Set Up
    children = []
    childrenFitness = []
    for i in range(0, constants.POPULATION_SIZE//2):
        print("Creating Child " + str(i+1) + "/" + str((constants.POPULATION_SIZE//2)))
        #Selection Criteria for parents
        indexParent1 = problem.selection(constants.POPULATION_SIZE)
        print("\tSelected Parent 1")
        indexParent2 = problem.selection(constants.POPULATION_SIZE)
        while indexParent1 == indexParent2:
            indexParent2 = problem.selection(constants.POPULATION_SIZE)
        print("\tSelected Parent 2")

        #Apply Crossover to generate offspring
        print("\tApplying Crossover")
        children.append(problem.crossover(population[indexParent1], population[indexParent2]))

        #Apply Mutation
        print("\tApplying Mutation")
        children[i] = problem.mutation(children[i], constants.MUTATION_RATE)

        #Validation
        print("\tValidating Child")
        children[i] = problem.validation(children[i])

        #Apply Local Search
        print("\tApplying Local Search")
        for j in range(0, constants.LOCAL_SEARCH_STEPS):
            print("\t\tLocal Search Step " + str(j+1)  + "/" + str((constants.LOCAL_SEARCH_STEPS)))
            children[i] = problem.localSearch(children[i])

        #Evaluate fitness
        print("\tEvaluating Child")
        ov = problem.objectiveValuePop(children[i], population)
        print("\t\tChild Score = " + str(ov))
        childrenFitness.append(ov)

    #Population Replacement
    print("Population Replacement")
    for i in range(0, len(children)):
        population, fitness = problem.populationReplacement(population, fitness, children[i], childrenFitness[i])

    #Print out the fitness of the end population
    print("\nFitness")
    print("Average Fitness = " + str(sum(fitness)/len(fitness)))
    print("Population Fitness = " + str(fitness))

    print("----------------------------------------------------------------------" + "\n")

#Print the end Time
print("End Time = " + str(datetime.now()))

#print out the best value
#TODO: Sort Out printing this
bestIndex = 0
bestFitness = fitness[bestIndex]
for i in range(1, constants.POPULATION_SIZE):
    if( problem.compareFitness(fitness[i], bestFitness) ):
        bestIndex = i
        bestFitness = fitness[i]
print("\n")
print("---------------------------Best  Individual---------------------------")
print(population[bestIndex])
print("Fitness = " + str(bestFitness))
print("----------------------------------------------------------------------" + "\n")
