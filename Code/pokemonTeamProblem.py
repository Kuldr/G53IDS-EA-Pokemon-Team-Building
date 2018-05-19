import constants
import random
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual
from pokemonTeamProblemHelperMethods import problemHelper

class pokemonTeamProblem:

    def compareFitness(self, fitness1, fitness2):
        if( fitness1 >= fitness2 ):
            return True
        else:
            return False

    def initialiseIndividual(self):
        # Initialises an individual by creating a team of 6 pokemon
        print("\tInitialising Pokemon 1")
        pokemon1 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        print("\tInitialising Pokemon 2")
        pokemon2 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        print("\tInitialising Pokemon 3")
        pokemon3 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        print("\tInitialising Pokemon 4")
        pokemon4 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        print("\tInitialising Pokemon 5")
        pokemon5 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()
        print("\tInitialising Pokemon 6")
        pokemon6 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else problemHelper.initialisePokemonIndividual()

        return pokemonTeamIndividual(pokemon1, pokemon2, pokemon3,
                                        pokemon4, pokemon5, pokemon6)

    def objectiveValuePop(self, individual, population):
        # Returns the average score vs the population
        score = 0
        teams = 0
        for i in range(0, len(population)):
            if( individual != population[i] ): #No point scoring against self
                print("\t\tScoring VS Team " + str(i))
                score += problemHelper.teamVTeam(individual, population[i])
                teams += 1
        return score/teams

    def selection(self, populationSize):
        #Randomly select any individual in the range
        return random.randrange(populationSize)

    def crossover(self, parent1, parent2):
        #Create a new individual where ~half the team memebers are from parent 1 and the other ~half are from parent 2

        #List of pokemon
        pokemon = [parent1.pokemon1, parent1.pokemon2, parent1.pokemon3,
                   parent1.pokemon4, parent1.pokemon5, parent1.pokemon6,
                   parent2.pokemon1, parent2.pokemon2, parent2.pokemon3,
                   parent2.pokemon4, parent2.pokemon5, parent2.pokemon6,]

        #This could create duplicates but that will be  dealt with in validation at a later step
        p1 = pokemon[random.randrange(len(pokemon))]
        p2 = pokemon[random.randrange(len(pokemon))]
        p3 = pokemon[random.randrange(len(pokemon))]
        p4 = pokemon[random.randrange(len(pokemon))]
        p5 = pokemon[random.randrange(len(pokemon))]
        p6 = pokemon[random.randrange(len(pokemon))]

        return pokemonTeamIndividual(p1, p2, p3, p4, p5, p6)

    def mutation(self, child, mutationRate):
        #Randomly mutate the individual based upon the mutation rate, then select a pokemon in the team and randomly mutate it in some way
        NUMBER_OF_MUTATIONS = 25

        if( random.random() <= mutationRate ):
            # Select a random team member to mutate
            pokemon = [child.pokemon1, child.pokemon2, child.pokemon3,
                       child.pokemon4, child.pokemon5, child.pokemon6]
            randPokeIndex = random.randrange(6)
            toMutate = pokemon[randPokeIndex]
            if( toMutate == None ):
                return child

            randMutate = random.randrange(0, NUMBER_OF_MUTATIONS)
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
        pokemon = [pokemonTeam.pokemon1, pokemonTeam.pokemon2,
                    pokemonTeam.pokemon3, pokemonTeam.pokemon4,
                    pokemonTeam.pokemon5, pokemonTeam.pokemon6]
        speciesID = []
        for i in range(0, len(pokemon)):
            if( pokemon[i] != None ):
                speciesID.append(pb.pokemon(pokemon[i].formID).species.id)
            else:
                speciesID.append(None)

        # Check for memebers with duplicate species
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

    def populationReplacement(self, population, fitness, child, childFitness):
        #Random Replacement but only if child is better or equal than previous member

        indexToChange = random.randrange(0, len(population))
        if( pokemonTeamProblem.compareFitness([], childFitness, fitness[indexToChange]) ):
            print("\tChild Replaced")
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness

    def localSearch(self, individual):
        #Apply a local search step and then return the new and improved individual
        population = []
        fitness = []

        #Do local search stuff here :)
        pokemon1Plus = problemHelper.changeIVS(individual.pokemon1, -3)
        pokemon2Plus = problemHelper.changeIVS(individual.pokemon2, -3)
        pokemon3Plus = problemHelper.changeIVS(individual.pokemon3, -3)
        pokemon4Plus = problemHelper.changeIVS(individual.pokemon4, -3)
        pokemon5Plus = problemHelper.changeIVS(individual.pokemon5, -3)
        pokemon6Plus = problemHelper.changeIVS(individual.pokemon6, -3)
        population.append(pokemonTeamIndividual(pokemon1Plus, pokemon2Plus,
                                                pokemon3Plus, pokemon4Plus,
                                                pokemon5Plus, pokemon6Plus))
        pokemon1Minus = problemHelper.changeIVS(individual.pokemon1, 3)
        pokemon2Minus = problemHelper.changeIVS(individual.pokemon2, 3)
        pokemon3Minus = problemHelper.changeIVS(individual.pokemon3, 3)
        pokemon4Minus = problemHelper.changeIVS(individual.pokemon4, 3)
        pokemon5Minus = problemHelper.changeIVS(individual.pokemon5, 3)
        pokemon6Minus = problemHelper.changeIVS(individual.pokemon6, 3)
        population.append(pokemonTeamIndividual(pokemon1Minus, pokemon2Minus,
                                                pokemon3Minus, pokemon4Minus,
                                                pokemon5Minus, pokemon6Minus))

        for i in range(0, len(population)):
            fitness.append(pokemonTeamProblem.objectiveValuePop([], population[i], population))

        bestIndex = 0
        bestFitness = fitness[bestIndex]
        for i in range(1, len(population)):
            if( pokemonTeamProblem.compareFitness([], fitness[i], bestFitness) ):
                bestIndex = i
                bestFitness = fitness[i]

        return population[bestIndex]