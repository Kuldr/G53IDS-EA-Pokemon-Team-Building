#TODO: MAKE THINGS LIKE EVs IVs MOVES GENERATE OFF A LIST SYSTEM

import constants
import random
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual
from pokemonTeamProblemHelperMethods import problemHelper

class pokemonTeamProblem:

    def initialiseIndividual(self):
        #TODO: Write top level comment
        #TODO: What if all members are none ???
        pokemon1 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        pokemon2 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        pokemon3 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        pokemon4 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        pokemon5 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        pokemon6 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        return pokemonTeamIndividual(pokemon1, pokemon2, pokemon3,
                                        pokemon4, pokemon5, pokemon6)

    def objectiveValue(self, individual):
        #Simple calculation of objective value based on the problem

        return None
        #return individual.x**2 + individual.y**2

    def selection(self, populationSize):
        #Randomly select any individual in the range
        return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        #Create a new individual where half the team memebers are from parent 1 and the other half are from parent 2
        #TODO: This is bad as each pokemon stays in the same team slot
        #TODO: This also doesn't do any crossover on the individual pokemon

        p1 = parent1.pokemon1
        p2 = parent1.pokemon2
        p3 = parent1.pokemon3
        p4 = parent2.pokemon4
        p5 = parent1.pokemon5
        p6 = parent1.pokemon6

        return pokemonTeamIndividual(p1, p2, p3, p4, p5, p6)

    # def mutation(self, child, mutationRate):
    #     #Randomly mutate the individual based upon the mutation rate, then randomly mutate either variable by multipling by a real number in the range (-3, 3)
    #
    #     NUMBER_OF_MUTATIONS = 1 #TODO: FIND A WAY TO AUTOMAGICALLY GENERATE THIS
    #     # MAYBE A LIST OF MUTATION FUNCTIONS THAT YOU RANDOMLY SELECT FROM
    #     # CAN YOU FIND OUT THE NUMBER OF METHODS IN ANOTHER CLASS
    #
    #     if( random.random() <= mutationRate ):
    #         # Select a random team member to mutate
    #         pokemon = [child.pokemon1, child.pokemon2, child.pokemon3,
    #                    child.pokemon4, child.pokemon5, child.pokemon6]
    #         randPokeIndex = random.randrange(6)
    #         toMutate = pokemon[randPokeIndex]
    #         r = random.randrange(NUMBER_OF_MUTATIONS)
    #         if( r == 0 ):
    #             # Ruin and recreate a random pokemon
    #             toMutate = self.initialisePokemonIndividual()
    #         elif( r == 1 ):
    #             # Randomly change the pokemon gender
    #
    #         elif( r == 2 ):
    #             # Randomly change the pokemon ability
    #
    #         elif( r == 3 ):
    #             # Randomly change the pokemon level
    #             toMutate.level = random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
    #             # TODO: INCREASE/DECREASE LEVEL AMOUNT
    #
    #         elif( r == 4 ):
    #             # Randomly change the pokemon shiny
    #             toMutate.shiny = random.choice([True, False])
    #
    #         elif( r == 5 ):
    #             # Randomly change the pokemon happiness
    #             toMutate.happiness = random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
    #             #TODO: INCREASE / DECREASE HAPPINESS AMOUNT
    #
    #         elif( r == 6 ):
    #             # Randomly change the pokemon nature
    #             toMutate.natureID = random.randrange(constants.MIN_NATUREID, constants.MAX_NATUREID+1)
    #
    #         elif( r == 7 ):
    #             # Randomly change nature to another nature with the same +ive
    #
    #         elif( r == 8 ):
    #             # Randomly change nature to another nature with the same -ive
    #
    #         elif( r == 9 ):
    #             # Ruin and Recreate the whole EVs
    #
    #         elif( r == 10 ):
    #             # Swap 2 sets of EVs
    #
    #         elif( r == 11 ):
    #             # Decrease 1 EV and increase another by a % ammount
    #
    #         elif( r == 12 ):
    #             # Decrease 1 EV and increase another by a integer ammount
    #
    #         elif( r == 13 ):
    #             # Ruin and Recreate the IVs
    #
    #         elif( r == 14 ):
    #             # Swap 2 sets of IVs
    #
    #         elif( r == 15 ):
    #             # Increase an IV by an ammount
    #
    #         elif( r == 16 ):
    #             # Decrease an IV by an ammount
    #
    #         # Pokemon Item - r&r, None
    #         # Pokemon Moves - r&r all, r&r one move, None
    #         # Pokemon Form - change form, evolve, devolve
    #
    #         if( randPokeIndex == 0 ):
    #             child.pokemon1 = toMutate
    #         if( randPokeIndex == 1 ):
    #             child.pokemon2 = toMutate
    #         if( randPokeIndex == 2 ):
    #             child.pokemon3 = toMutate
    #         if( randPokeIndex == 3 ):
    #             child.pokemon4 = toMutate
    #         if( randPokeIndex == 4 ):
    #             child.pokemon5 = toMutate
    #         if( randPokeIndex == 5 ):
    #             child.pokemon6 = toMutate
    #     return child
    #
    #     # if( random.random() <= mutationRate ):
    #     #     if( random.randrange(2) == 0 ):
    #     #         child.x *= random.uniform(-3.0, 3.0)
    #     #     else:
    #     #         child.y *= random.uniform(-3.0, 3.0)
    #     # return child
    #
    def validation(self, pokemonTeam):
        # TODO: THE REST OF THE GA ISN'T BUILT TO HANDLE NONE MEMBERS
        pokemon = [pokemonTeam.pokemon1, pokemonTeam.pokemon2,
                    pokemonTeam.pokemon3, pokemonTeam.pokemon4,
                    pokemonTeam.pokemon5, pokemonTeam.pokemon6]
        #TODO: WHAT IF NONE
        speciesID = []
        for i in range(0, len(pokemon)):
            x = 1
            if( pokemon[i] != None ):
                speciesID.append(pb.pokemon(pokemon[i].formID).species.id)

        # Check for memebers with duplicate species
        # TODO: THIS IS HELLA UGLY # MAYBE COULD BE DONE WITH A COUPLE OF FOR LOOPS
        if( speciesID[0] == speciesID[1] or
            speciesID[0] == speciesID[2] or
            speciesID[0] == speciesID[3] or
            speciesID[0] == speciesID[4] or
            speciesID[0] == speciesID[5]):
                pokemon[0] = None
        if( speciesID[1] == speciesID[2] or
            speciesID[1] == speciesID[3] or
            speciesID[1] == speciesID[4] or
            speciesID[1] == speciesID[5]):
                pokemon[1] = None
        if( speciesID[2] == speciesID[3] or
            speciesID[2] == speciesID[4] or
            speciesID[2] == speciesID[5]):
                pokemon[2] = None
        if( speciesID[3] == speciesID[4] or
            speciesID[3] == speciesID[5]):
                pokemon[3] = None
        if( speciesID[4] == speciesID[5]):
                pokemon[4] = None

        # Validate each individual pokemon
        for i in range(0, len(pokemon)):
            if( pokemon[i] != None ):
                pokemon[i] = problemHelper.validatePokemonIndividual(pokemon[i])

        pokemonTeam.pokemon1 = pokemon[0]
        pokemonTeam.pokemon2 = pokemon[1]
        pokemonTeam.pokemon3 = pokemon[2]
        pokemonTeam.pokemon4 = pokemon[3]
        pokemonTeam.pokemon5 = pokemon[4]
        pokemonTeam.pokemon6 = pokemon[5]

        return pokemonTeam

    def populationReplacement(self, population, fitness, child, childFitness, populationSize):
        #Random Replacement but only if child is better than previous member

        indexToChange = random.randrange(populationSize)
        if( fitness[indexToChange] > childFitness ):
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness
