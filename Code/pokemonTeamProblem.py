#TODO: MAKE THINGS LIKE EVs IVs MOVES GENERATE OFF A LIST SYSTEM

import constants
import random
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual
from pokemonTeamProblemHelperMethods import problemHelper

import testPokemon

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

    def objectiveValuePop(self, individual, population):
        # Returns the average score vs the population
        score = 0
        for i in range(0, len(population)):
            if( individual != population[i] ): #No point scoring against self
                score += problemHelper.teamVTeam(individual, population[i])

        return score/(len(population)-1)

    # def objectiveValue(self, individual):
    #     #Simple calculation of objective value based on the problem
    #
    #     score = 0
    #
    #     pokemon = []
    #     if( individual.pokemon1 != None ):
    #         pokemon.append(individual.pokemon1)
    #     if( individual.pokemon2 != None ):
    #         pokemon.append(individual.pokemon2)
    #     if( individual.pokemon3 != None ):
    #         pokemon.append(individual.pokemon3)
    #     if( individual.pokemon4 != None ):
    #         pokemon.append(individual.pokemon4)
    #     if( individual.pokemon5 != None ):
    #         pokemon.append(individual.pokemon5)
    #     if( individual.pokemon6 != None ):
    #         pokemon.append(individual.pokemon6)
    #
    #     #Do checks to individual pokemon
    #     for i in range(0, len(pokemon)):
    #         #Item Scoring code - Gives points based upon
    #         if( pokemon[i].itemID != None ):
    #             attributes = pb.item(pokemon[i].itemID).attributes
    #             holdableActive = False
    #             for i in range(0, len(attributes)):
    #                 if( attributes[i].id == pb.item_attribute("holdable-active").id ):
    #                     holdableActive = True
    #             if( holdableActive == True ):
    #                 score += constants.ITEM_POINTS
    #
    #
    #     return score
    #     #return individual.x**2 + individual.y**2

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

    def mutation(self, child, mutationRate):
        #Randomly mutate the individual based upon the mutation rate, then randomly mutate either variable by multipling by a real number in the range (-3, 3)

        # Mutation doesn't care for validation this will happen afterwards and if it is invalid sorted out in validation
        # Although where validation can be controlled it is

        #TODO: ONLY WRITEN MUTATION ON INDIVIDUAL POKEMON NOT THE TEAM

        NUMBER_OF_MUTATIONS = 24 #TODO: FIND A WAY TO AUTOMAGICALLY GENERATE THIS
        # MAYBE A LIST OF MUTATION FUNCTIONS THAT YOU RANDOMLY SELECT FROM
        # CAN YOU FIND OUT THE NUMBER OF METHODS IN ANOTHER CLASS

        if( random.random() <= mutationRate ):
            # Select a random team member to mutate
            pokemon = [child.pokemon1, child.pokemon2, child.pokemon3,
                       child.pokemon4, child.pokemon5, child.pokemon6]
            randPokeIndex = random.randrange(6)
            toMutate = pokemon[randPokeIndex]
            if( toMutate == None ):
                return child

            # Tested all mutations up to 24
            randMutate = random.randrange(0, NUMBER_OF_MUTATIONS+1)
            if( randMutate == 0 ):
                # Ruin and recreate a random pokemon
                toMutate = problemHelper.initialisePokemonIndividual()
            elif( randMutate == 1 ):
                # Ruin and Recreate the gender
                toMutate.gender = problemHelper.initialiseGender(pb.pokemon(toMutate.formID))
            elif( randMutate == 2 ):
                # Randomly change the pokemon ability
                toMutate.ability = problemHelper.initialiseAbility(pb.pokemon(toMutate.formID))
            elif( randMutate == 3 ):
                # Ruin and Recreate the pokemon level
                toMutate.level = random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
            elif( randMutate == 4 ):
                # Increase the level by a random amount
                toMutate.level += random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
            elif( randMutate == 5 ):
                # Decrease the level by a random amount
                toMutate.level -= random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
            elif( randMutate == 6 ):
                # Ruin and Recreate shiny status
                toMutate.shiny = random.choice([True, False])
            elif( randMutate == 7 ):
                # Ruin and Recreate the pokemon happiness
                toMutate.happiness = random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
            elif( randMutate == 8 ):
                # Increase the Happiness by a random amount
                toMutate.happiness += random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
            elif( randMutate == 9 ):
                # Decrease the Happiness by a random amount
                toMutate.happiness -= random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
            elif( randMutate == 10 ):
                # Randomly change the pokemon nature
                toMutate.natureID = random.randrange(constants.MIN_NATUREID, constants.MAX_NATUREID+1)
            elif( randMutate == 11 ):
                # Randomly change nature to another nature with the same +ive
                    # THIS CAN RANDOMLY GENERATE THE SAME NATURE
                incStat = pb.nature(toMutate.natureID).increased_stat
                if( incStat != None ): # Check there is an increased stat
                    sameIncrease = []
                    for i in range(constants.MIN_NATUREID, constants.MAX_NATUREID):
                        if( pb.nature(i).increased_stat != None and pb.nature(i).increased_stat.id == incStat.id ):
                            sameIncrease.append(pb.nature(i).id)
                    toMutate.natureID = sameIncrease[random.randrange(0, len(sameIncrease))]
            elif( randMutate == 12 ):
                # Randomly change nature to another nature with the same -ive
                    # THIS CAN RANDOMLY GENERATE THE SAME NATURE
                decStat = pb.nature(toMutate.natureID).decreased_stat
                if( decStat != None ): # Check there is an increased stat
                    sameDecrease = []
                    for i in range(constants.MIN_NATUREID, constants.MAX_NATUREID):
                        if( pb.nature(i).decreased_stat != None and pb.nature(i).decreased_stat.id == decStat.id ):
                            sameDecrease.append(pb.nature(i).id)
                    toMutate.natureID = sameDecrease[random.randrange(0, len(sameDecrease))]
            elif( randMutate == 13 ):
                # Ruin and Recreate the whole EVs
                toMutate.evHP, toMutate.evAtk, toMutate.evDef, toMutate.evSpA, toMutate.evSpD, toMutate.evSpe = problemHelper.initialiesEVs()
            elif( randMutate == 14 ):
                # Swap 2 sets of EVs
                    # Can swap an EV with itself
                EVs = [toMutate.evHP, toMutate.evAtk, toMutate.evDef,
                        toMutate.evSpA, toMutate.evSpD, toMutate.evSpe]
                evIndex1 = random.randrange(0, len(EVs))
                evIndex2 = random.randrange(0, len(EVs))
                temp = EVs[evIndex1]
                EVs[evIndex1] = EVs[evIndex2]
                EVs[evIndex2] = temp

                toMutate.evHP = EVs[0]
                toMutate.evAtk = EVs[1]
                toMutate.evDef = EVs[2]
                toMutate.evSpA = EVs[3]
                toMutate.evSpD = EVs[4]
                toMutate.evSpe = EVs[5]
            elif( randMutate == 15 ):
                # Decrease 1 EV and increase another by an ammount
                    # Can swap an EV with itself
                EVs = [toMutate.evHP, toMutate.evAtk, toMutate.evDef,
                        toMutate.evSpA, toMutate.evSpD, toMutate.evSpe]
                evIndex1 = random.randrange(0, len(EVs))
                evIndex2 = random.randrange(0, len(EVs))

                amountToChange =  random.randrange(constants.MIN_EV, constants.MAX_EV)
                # Make sure that you don't go over any boundaries
                if( EVs[evIndex1] - amountToChange < constants.MIN_EV ):
                    amountToChange = EVs[evIndex1]
                if( EVs[evIndex2] + amountToChange > constants.MAX_EV ):
                    amountToChange = EVs[evIndex2]

                EVs[evIndex1] = EVs[evIndex1] - amountToChange
                EVs[evIndex2] = EVs[evIndex2] + amountToChange

                toMutate.evHP = EVs[0]
                toMutate.evAtk = EVs[1]
                toMutate.evDef = EVs[2]
                toMutate.evSpA = EVs[3]
                toMutate.evSpD = EVs[4]
                toMutate.evSpe = EVs[5]
            elif( randMutate == 16 ):
                # Ruin and Recreate the IVs
                toMutate.ivHP, toMutate.ivAtk, toMutate.ivDef, toMutate.ivSpA, toMutate.ivSpD, toMutate.ivSpe = problemHelper.initialiseIVs()
            elif( randMutate == 17 ):
                # Swap 2 sets of IVs
                    # Can swap an IV with itself
                IVs = [toMutate.ivHP, toMutate.ivAtk, toMutate.ivDef,
                        toMutate.ivSpA, toMutate.ivSpD, toMutate.ivSpe]
                ivIndex1 = random.randrange(0, len(IVs))
                ivIndex2 = random.randrange(0, len(IVs))
                temp = IVs[ivIndex1]
                IVs[ivIndex1] = IVs[ivIndex2]
                IVs[ivIndex2] = temp

                toMutate.ivHP = IVs[0]
                toMutate.ivAtk = IVs[1]
                toMutate.ivDef = IVs[2]
                toMutate.ivSpA = IVs[3]
                toMutate.ivSpD = IVs[4]
                toMutate.ivSpe = IVs[5]
            elif( randMutate == 18 ):
                # Increase an IV by an ammount
                ivChange = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
                r = random.randrange(0, constants.NUMBER_OF_STATS)
                if( r == 0 ):
                    toMutate.ivHP += ivChange
                    if( toMutate.ivHP > constants.MAX_IV ):
                        toMutate.ivHP = constants.MAX_IV
                elif( r == 1 ):
                    toMutate.ivAtk += ivChange
                    if( toMutate.ivAtk > constants.MAX_IV ):
                        toMutate.ivAtk = constants.MAX_IV
                elif( r == 2 ):
                    toMutate.ivDef += ivChange
                    if( toMutate.ivDef > constants.MAX_IV ):
                        toMutate.ivDef = constants.MAX_IV
                elif( r == 3 ):
                    toMutate.ivSpA += ivChange
                    if( toMutate.ivSpA > constants.MAX_IV ):
                        toMutate.ivSpA = constants.MAX_IV
                elif( r == 4 ):
                    toMutate.ivSpD += ivChange
                    if( toMutate.ivSpD > constants.MAX_IV ):
                        toMutate.ivSpD = constants.MAX_IV
                elif( r == 5 ):
                    toMutate.ivSpe += ivChange
                    if( toMutate.ivSpe > constants.MAX_IV ):
                        toMutate.ivSpe = constants.MAX_IV
            elif( randMutate == 19 ):
                # Decrease an IV by an ammount
                ivChange = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
                r = random.randrange(0, constants.NUMBER_OF_STATS)
                if( r == 0 ):
                    toMutate.ivHP -= ivChange
                    if( toMutate.ivHP < constants.MIN_IV ):
                        toMutate.ivHP = constants.MIN_IV
                elif( r == 1 ):
                    toMutate.ivAtk -= ivChange
                    if( toMutate.ivAtk < constants.MIN_IV ):
                        toMutate.ivAtk = constants.MIN_IV
                elif( r == 2 ):
                    toMutate.ivDef -= ivChange
                    if( toMutate.ivDef < constants.MIN_IV ):
                        toMutate.ivDef = constants.MIN_IV
                elif( r == 3 ):
                    toMutate.ivSpA -= ivChange
                    if( toMutate.ivSpA < constants.MIN_IV ):
                        toMutate.ivSpA = constants.MIN_IV
                elif( r == 4 ):
                    toMutate.ivSpD -= ivChange
                    if( toMutate.ivSpD < constants.MIN_IV ):
                        toMutate.ivSpD = constants.MIN_IV
                elif( r == 5 ):
                    toMutate.ivSpe -= ivChange
                    if( toMutate.ivSpe < constants.MIN_IV ):
                        toMutate.ivSpe = constants.MIN_IV
            elif( randMutate == 20 ):
                # Ruin and Recreate item
                toMutate.itemID = problemHelper.initialiseItem()
            elif( randMutate == 21 ):
                # Set item to None
                toMutate.itemID = None
            elif( randMutate == 22 ):
                # Ruin and Recreate all moves
                toMutate.move1, toMutate.move2, toMutate.move3, toMutate.move4 = problemHelper.initialiseMoves(pb.pokemon(toMutate.formID))
            elif( randMutate == 23 ):
                # Ruin and Recreate one move
                moveChange, _, _, _ = problemHelper.initialiseMoves(pb.pokemon(toMutate.formID)) # I hope that this works by just taking the first one :)
                r = random.randrange(0, constants.NUMBER_OF_MOVES)
                if( r == 0 ):
                    toMutate.move1 = moveChange
                elif( r == 1 ):
                    toMutate.move2 = moveChange
                elif( r == 2 ):
                    toMutate.move3 = moveChange
                elif( r == 3 ):
                    toMutate.move4 = moveChange
            elif( randMutate == 24 ):
                # Set random move to None
                r = random.randrange(0, constants.NUMBER_OF_MOVES)
                if( r == 0 ):
                    toMutate.move1 = None
                elif( r == 1 ):
                    toMutate.move2 = None
                elif( r == 2 ):
                    toMutate.move3 = None
                elif( r == 3 ):
                    toMutate.move4 = None
            # Pokemon Form - change form, evolve, devolve
            # Set nature to a nuetral one

            if( randPokeIndex == 0 ):
                child.pokemon1 = toMutate
            if( randPokeIndex == 1 ):
                child.pokemon2 = toMutate
            if( randPokeIndex == 2 ):
                child.pokemon3 = toMutate
            if( randPokeIndex == 3 ):
                child.pokemon4 = toMutate
            if( randPokeIndex == 4 ):
                child.pokemon5 = toMutate
            if( randPokeIndex == 5 ):
                child.pokemon6 = toMutate
        return child

    def validation(self, pokemonTeam):
        # TODO: THE REST OF THE GA ISN'T BUILT TO HANDLE NONE MEMBERS
        pokemon = [pokemonTeam.pokemon1, pokemonTeam.pokemon2,
                    pokemonTeam.pokemon3, pokemonTeam.pokemon4,
                    pokemonTeam.pokemon5, pokemonTeam.pokemon6]
        #TODO: WHAT IF NONE
        speciesID = []
        for i in range(0, len(pokemon)):
            if( pokemon[i] != None ):
                speciesID.append(pb.pokemon(pokemon[i].formID).species.id)
            else:
                speciesID.append(None)

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
            print("Child Replaced")
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness
