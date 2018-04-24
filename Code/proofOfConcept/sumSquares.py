import random
from proofOfConcept.sumSquaresIndividual import sumSquaresIndividual

class sumSquares:

    def compareFitness(self, fitness1, fitness2):
        if( fitness1 <= fitness2 ):
            return True
        else:
            return False

    def initialiseIndividual(self):
        #Initialises all the Individuals to random integer in the range
        return sumSquaresIndividual(random.randrange(-5, 5),random.randrange(-5, 5))

    def objectiveValuePop(self, individual, population):
        #Simple calculation of objective value based on the problem
        return individual.x**2 + individual.y**2

    def selection(self, populationSize):
        #Randomly select any individual in the range
        return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        #Create a new individual where the first element comes from the first parent and the second from the second parent
        return sumSquaresIndividual(parent1.x, parent2.y)

    def mutation(self, child, mutationRate):
        #Randomly mutate the individual based upon the mutation rate, then randomly mutate either variable by multipling by a real number in the range (-3, 3)
        if( random.random() <= mutationRate ):
            if( random.randrange(2) == 0 ):
                child.x *= random.uniform(-3.0, 3.0)
            else:
                child.y *= random.uniform(-3.0, 3.0)
        return child

    def validation(self, child):
        #Validate the individuals by moving them back into the valid range
        if( child.x > 5 ):
            child.x = 5
        if( child.y > 5 ):
            child.y = 5
        if( child.x < -5 ):
            child.x = -5
        if( child.y < -5 ):
            child.y = -5
        return child

    def populationReplacement(self, population, fitness, child, childFitness):
        #Random Replacement but only if child is better than previous member
        indexToChange = random.randrange(0, len(population))
        if( sumSquares.compareFitness([], childFitness, fitness[indexToChange]) ):
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness

    def localSearch(self, individual):
        #Apply a local search step and then return the new and improved individual
        population = []
        fitness = []
        population.append(sumSquaresIndividual(individual.x+0.01,
                                                    individual.y+0.01))
        population.append(sumSquaresIndividual(individual.x+0.01,
                                                    individual.y))
        population.append(sumSquaresIndividual(individual.x+0.01,
                                                    individual.y-0.01))
        population.append(sumSquaresIndividual(individual.x,
                                                    individual.y+0.01))
        population.append(sumSquaresIndividual(individual.x,
                                                    individual.y))
        population.append(sumSquaresIndividual(individual.x,
                                                    individual.y-0.01))
        population.append(sumSquaresIndividual(individual.x-0.01,
                                                    individual.y+0.01))
        population.append(sumSquaresIndividual(individual.x-0.01,
                                                    individual.y))
        population.append(sumSquaresIndividual(individual.x-0.01,
                                                    individual.y-0.01))
        for i in range(0, len(population)):
            fitness.append(sumSquares.objectiveValuePop([], population[i], population))

        bestIndex = 0
        bestFitness = fitness[bestIndex]
        for i in range(1, len(population)):
            if( sumSquares.compareFitness([], fitness[i], bestFitness)):
                bestIndex = i
                bestFitness = fitness[i]

        return population[bestIndex]
