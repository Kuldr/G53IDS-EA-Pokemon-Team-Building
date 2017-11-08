import random

class xSquared:

    def initialiseIndividual(self):
        return [random.randrange(-5, 5),random.randrange(-5, 5)]

    def objectiveValue(self, individual):
        return individual[0]**2 + individual[1]**2

    def selection(self, populationSize):
        return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        return [parent1[0], parent2[1]]

    def mutation(self, child, mutationRate):
        if( random.random() <= mutationRate ):
            child[random.randrange(2)] *= random.uniform(-3.0, 3.0)
        return child

    def validation(self, child):
        if( child[0] > 10 ):
            child[0] = 10
        if( child[1] > 10 ):
            child[1] = 10
        if( child[0] < -10 ):
            child[0] = -10
        if( child[1] < -10 ):
            child[1] = -10
        return child

    def populationReplacement(self, population, fitness, child, childFitness, populationSize):
        #Random Replacement but only if child is better than previous member
        indexToChange = random.randrange(populationSize)
        if( fitness[indexToChange] > childFitness ):
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness
