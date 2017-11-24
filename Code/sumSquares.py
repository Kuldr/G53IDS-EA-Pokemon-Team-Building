import random
from sumSquaresIndividual import sumSquaresIndividual

class sumSquares:

    def initialiseIndividual(self):
        return sumSquaresIndividual(random.randrange(-5, 5),random.randrange(-5, 5))

    def objectiveValue(self, individual):
        return individual.x**2 + individual.y**2

    def selection(self, populationSize):
        return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        return sumSquaresIndividual(parent1.x, parent2.y)

    def mutation(self, child, mutationRate):
        if( random.random() <= mutationRate ):
            if( random.randrange(2) == 0 ):
                child.x *= random.uniform(-3.0, 3.0)
            else:
                child.y *= random.uniform(-3.0, 3.0)
        return child

    def validation(self, child):
        if( child.x > 10 ):
            child.x = 10
        if( child.y > 10 ):
            child.y = 10
        if( child.x < -10 ):
            child.x = -10
        if( child.y < -10 ):
            child.y = -10
        return child

    def populationReplacement(self, population, fitness, child, childFitness, populationSize):
        #Random Replacement but only if child is better than previous member
        indexToChange = random.randrange(populationSize)
        if( fitness[indexToChange] > childFitness ):
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness
