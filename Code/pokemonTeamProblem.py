import random
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual

class pokemonTeamProblem:

    def initialiseIndividual(self):
        #TODO: Initialises all the Individuals to random integer in the range
        #TODO: What if I want it to be None
        pokemon1 = self.initialisePokemonIndividual()
        pokemon2 = self.initialisePokemonIndividual()
        pokemon3 = self.initialisePokemonIndividual()
        pokemon4 = self.initialisePokemonIndividual()
        pokemon5 = self.initialisePokemonIndividual()
        pokemon6 = self.initialisePokemonIndividual()
        return pokemonTeamIndividual(pokemon1, pokemon2, pokemon3,
                                        pokemon4, pokemon5, pokemon6)
        # return sumSquaresIndividual(random.randrange(-5, 5),random.randrange(-5, 5))

    def initialisePokemonIndividual(self):
        #TODO: First made it to just make a pokemon not bothered about validation
        #TODO Need to make somethings be able to be None - This can be a variable in the constants file
        #TODO Add the limits into constants file

        #Only generates default forms later is used to select other forms
        formID = random.randrange(0,802)+1
        # 1-802 but that doesn't get forms
        # TODO: IF THE POKEMON HAS FORMS SELECT ONE AT RANDOM ??? HOW


        #itemID = 213 #TODO What is the valid range ARRRRGGGGGGGHHHHHH
        # Only want holdable items
        itemID = random.randrange(0,918)+1

        level = random.randrange(0, 100)+1
        shiny = random.choice([True, False])
        happiness = random.randrange(0, 256)
        natureID = random.randrange(0, 25)+1
        #TODO: EVs can add up to over 510
        evHP = random.randrange(0, 256)
        evAtk = random.randrange(0, 256)
        evDef = random.randrange(0, 256)
        evSpA = random.randrange(0, 256)
        evSpD = random.randrange(0, 256)
        evSpe = random.randrange(0, 256)
        ivHP = random.randrange(0, 32)
        ivAtk = random.randrange(0, 32)
        ivDef = random.randrange(0, 32)
        ivSpA = random.randrange(0, 32)
        ivSpD = random.randrange(0, 32)
        ivSpe = random.randrange(0, 32)

        #Pokemon dependant info so references the pokemon to get relevant info
        formID = formID #Choose a new form if relevant #TODO
        p = pb.pokemon(formID) #Get the pokemon to reference

        abilityIndex = random.randrange(0, len(p.abilities)) #Gives a random number to index the abilities
        ability = p.abilities[abilityIndex].slot #Gets the slot number for that ability index

        gender = random.randrange(0,3)+1 #TODO: FIX THIS SO THAT YOU CAN ONLY GET CORRECT GENDERS BUT AINT TOO BOTHERED FOR NOW

        # TODO: THIS CAN TECHNICALLY CREATE THE SAME MOVE TWICE
        moveIndex = random.randrange(0, len(p.moves))
        move1 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move2 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move3 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move4 = p.moves[moveIndex].move.id


        return pokemonIndividual(formID, gender, itemID, ability, level, shiny,
                        happiness, natureID,
                        evHP, evAtk, evDef, evSpA, evSpD, evSpe,
                        ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe,
                        move1, move2, move3, move4)

    def objectiveValue(self, individual):
        #Simple calculation of objective value based on the problem

        return None
        #return individual.x**2 + individual.y**2

    def selection(self, populationSize):
        #Randomly select any individual in the range

        return None
        #return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        #Create a new individual where the first element comes from the first parent and the second from the second parent

        return None
        #return sumSquaresIndividual(parent1.x, parent2.y)

    def mutation(self, child, mutationRate):
        #Randomly mutate the individual based upon the mutation rate, then randomly mutate either variable by multipling by a real number in the range (-3, 3)

        return None
        # if( random.random() <= mutationRate ):
        #     if( random.randrange(2) == 0 ):
        #         child.x *= random.uniform(-3.0, 3.0)
        #     else:
        #         child.y *= random.uniform(-3.0, 3.0)
        # return child

    def validation(self, child):
        #Validate the individuals by moving them back into the valid range

        return None
        # if( child.x > 5 ):
        #     child.x = 5
        # if( child.y > 5 ):
        #     child.y = 5
        # if( child.x < -5 ):
        #     child.x = -5
        # if( child.y < -5 ):
        #     child.y = -5
        # return child

    def populationReplacement(self, population, fitness, child, childFitness, populationSize):
        #Random Replacement but only if child is better than previous member

        return None
        # indexToChange = random.randrange(populationSize)
        # if( fitness[indexToChange] > childFitness ):
        #     population[indexToChange] = child
        #     fitness[indexToChange] = childFitness
        # return population, fitness
