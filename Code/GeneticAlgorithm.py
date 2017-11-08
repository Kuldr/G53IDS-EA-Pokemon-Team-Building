#IMPORTS
import random

import constants

#Initialise and evaluate population

#Termination Criteria loop, runs for a set number of generations
for x in range(0, constants.NUMBER_OF_GENERATIONS):
    #Main GA loop
    for i in range(0, constants.POPULATION_SIZE/2):
        print(random.randrange(constants.POPULATION_SIZE))
        #Selection Criteria for parents
        #Currently just random for simplictity
        indexParent1 = random.randrange(constants.POPULATION_SIZE)
        indexParent2 = random.randrange(constants.POPULATION_SIZE)

        #Apply Crossover to generate offspring

        #Apply Mutation

    #Population Replacement
