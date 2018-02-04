#TODO: MAKE THINGS LIKE EVs IVs MOVES GENERATE OFF A LIST SYSTEM

import constants
import random
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual

class pokemonTeamProblem:

    def initialiseIndividual(self):
        #TODO: Write top level comment
        #TODO: What if all members are none ???
        pokemon1 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        pokemon2 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        pokemon3 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        pokemon4 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        pokemon5 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        pokemon6 = None if random.random() <= constants.NO_TEAM_MEMBER_RATE else self.initialisePokemonIndividual()
        return pokemonTeamIndividual(pokemon1, pokemon2, pokemon3,
                                        pokemon4, pokemon5, pokemon6)
        # return sumSquaresIndividual(random.randrange(-5, 5),random.randrange(-5, 5))

    def initialisePokemonIndividual(self):
        #TODO: First made it to just make a pokemon not bothered about validation
        #TODO Need to make somethings be able to be None - This can be a variable in the constants file
        #TODO Add the limits into constants file

        # Generates the default form and later on checks for other forms
        formID = random.randrange(constants.MIN_FORMID, constants.MAX_FORMID+1)

        # Write the item as teneray opperators like pokemon generation
        itemID = None if random.random() <= constants.NO_HELD_ITEM_RATE else self.initialiseItem()

        level = random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
        shiny = random.choice([True, False])
        happiness = random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
        natureID = random.randrange(constants.MIN_NATUREID, constants.MAX_NATUREID+1)
        ivHP = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
        ivAtk = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
        ivDef = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
        ivSpA = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
        ivSpD = random.randrange(constants.MIN_IV, constants.MAX_IV+1)
        ivSpe = random.randrange(constants.MIN_IV, constants.MAX_IV+1)

        #Initialise EVs to 0
        evHP = constants.MIN_EV
        evAtk = constants.MIN_EV
        evDef = constants.MIN_EV
        evSpA = constants.MIN_EV
        evSpD = constants.MIN_EV
        evSpe = constants.MIN_EV
        # Randomly distribute EVs 1 by 1
        #TODO: DOES IT MATTER THAT THIS GIVES OUT ALL OF THE EVs
        #TODO: DOES IT MATTER THAT THE EV SPREAD WILL BE ~85 for all stats
        #TODO: COULD GENERATE 4 AT A TIME AS THAT IS ALL THAT MATTERS (508)
        #TODO: NEED TO VALIDATE THAT YOU DON'T HAVE ANY STAT OVER 256
        #TODO: MAKE SUB METHOD SO MUTATION CAN ACCESS THIS
        for _ in range(0, constants.MAX_EV_TOTAL):
            r = random.randrange(0, 6)
            if( r == 0):
                evHP += 1
            elif( r == 1 ):
                evAtk += 1
            elif( r == 2 ):
                evDef += 1
            elif( r == 3 ):
                evSpA += 1
            elif( r == 4 ):
                evSpD += 1
            elif( r == 5 ):
                evSpe += 1

        #Pokemon dependant info so references the pokemon to get relevant info
        formVarieties = pb.pokemon(formID).species.varieties
        formRand = random.randrange(0, len(formVarieties))
        formID = formVarieties[formRand].pokemon.id # Update the formID into new form
        #TODO: CHECK IF FORM IS VALID IN BATTLE
        # pb.pokemon(formID).forms[0].is_battle.only
        # Mimikyu forms like disguised and totem come to mind

        p = pb.pokemon(formID) #Get the pokemon to reference

        abilityIndex = random.randrange(0, len(p.abilities)) #Gives a random number to index the abilities
        ability = p.abilities[abilityIndex].slot #Gets the slot number for that ability index

        #Randomly generates a gender but at the correct ratio
        gr = p.species.gender_rate #Gender Rate is given as x, where x/8 gives the chance of being female unless x = -1 where then the pokemon is genderless
        if( gr == -1 ):
            gender = pb.gender("genderless").id
        elif( gr == 0 ):
            gender = pb.gender("male").id
        elif( gr == 8 ):
            gender = pb.gender("female").id
        else:
            grand = random.randrange(0,8)+1
            if( grand <= gr ):
                gender = pb.gender("female").id
            else:
                gender = pb.gender("male").id

        # Make move indexing some kind of list for generation and Validation
        # This could also make it so that checking for dupes is easier

        moves = []
        for i in range(0, constants.MAX_MOVES):
            moves.append(None if random.random() <= constants.NO_MOVE_RATE else p.moves[random.randrange(0, len(p.moves))].move.id)
        move1 = moves[0]
        move2 = moves[1]
        move3 = moves[2]
        move4 = moves[3]

        #Check and remove move duplication
        if( move1 == move2 or move1 == move3 or move1 == move4 ):
            print("Duplicate Move") #DEBUG
            move1 = None
        if( move2 == move3 or move2 == move4 ):
            print("Duplicate Move") #DEBUG
            move2 = None
        if( move3== move4 ):
            print("Duplicate Move") #DEBUG
            move3 = None

        # Check for no moves
        if( move1 == None and move2 == None and move3 == None and move4 == None):
            move1 = p.moves[random.randrange(0, len(p.moves))].move.id

        return pokemonIndividual(formID, gender, itemID, ability, level, shiny,
                        happiness, natureID,
                        evHP, evAtk, evDef, evSpA, evSpD, evSpe,
                        ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe,
                        move1, move2, move3, move4)

    def initialiseItem(self):
        itemID = random.randrange(constants.MIN_ITEMID, constants.MAX_ITEMID+1)
        while self.validateItemID(itemID) == None:
            itemID = random.randrange(constants.MIN_ITEMID, constants.MAX_ITEMID+1)
        return itemID


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

    def mutation(self, child, mutationRate):
        #Randomly mutate the individual based upon the mutation rate, then randomly mutate either variable by multipling by a real number in the range (-3, 3)

        return None
        # if( random.random() <= mutationRate ):
        #     if( random.randrange(2) == 0 ):
        #         child.x *= random.uniform(-3.0, 3.0)
        #     else:
        #         child.y *= random.uniform(-3.0, 3.0)
        # return child

    def validation(self, pokemonTeam):
        # TODO: THE REST OF THE GA ISN'T BUILT TO HANDLE NONE MEMBERS
        pokemon = [pokemonTeam.pokemon1, pokemonTeam.pokemon2,
                    pokemonTeam.pokemon3, pokemonTeam.pokemon4,
                    pokemonTeam.pokemon5, pokemonTeam.pokemon6]
        pbPokemon = [pb.pokemon(pokemon[0].formID),
                     pb.pokemon(pokemon[1].formID),
                     pb.pokemon(pokemon[2].formID),
                     pb.pokemon(pokemon[3].formID),
                     pb.pokemon(pokemon[4].formID),
                     pb.pokemon(pokemon[5].formID)]

        # Check for memebers with duplicate species
        # TODO: THIS IS HELLA UGLY
        if( pbPokemon[0].species.id == pbPokemon[1].species.id or
            pbPokemon[0].species.id == pbPokemon[2].species.id or
            pbPokemon[0].species.id == pbPokemon[3].species.id or
            pbPokemon[0].species.id == pbPokemon[4].species.id or
            pbPokemon[0].species.id == pbPokemon[5].species.id):
                pokemon[0] = None
        if( pbPokemon[1].species.id == pbPokemon[2].species.id or
            pbPokemon[1].species.id == pbPokemon[3].species.id or
            pbPokemon[1].species.id == pbPokemon[4].species.id or
            pbPokemon[1].species.id == pbPokemon[5].species.id):
                pokemon[1] = None
        if( pbPokemon[2].species.id == pbPokemon[3].species.id or
            pbPokemon[2].species.id == pbPokemon[4].species.id or
            pbPokemon[2].species.id == pbPokemon[5].species.id):
                pokemon[2] = None
        if( pbPokemon[3].species.id == pbPokemon[4].species.id or
            pbPokemon[3].species.id == pbPokemon[5].species.id):
                pokemon[3] = None
        if( pbPokemon[4].species.id == pbPokemon[5].species.id):
                pokemon[4] = None

        # Validate each individual pokemon
        for i in range(0, len(pokemon)):
            if( pokemon[i] != None ):
                pokemon[i] = self.validatePokemonIndividual(pokemon[i])

        pokemonTeam.pokemon1 = pokemon[0]
        pokemonTeam.pokemon2 = pokemon[1]
        pokemonTeam.pokemon3 = pokemon[2]
        pokemonTeam.pokemon4 = pokemon[3]
        pokemonTeam.pokemon5 = pokemon[4]
        pokemonTeam.pokemon6 = pokemon[5]

        return pokemonTeam

    def validatePokemonIndividual(self, pokemonChild):
        #Validate the individuals by making them None if invalid in anyway
        # TODO: Possibly not the best approach
        # TODO: ADD IN ERROR PRINT OUT FOR WHAT FAILED
        # TODO: SEPERATE ERROR/DEBUG AND INTENTIONAL OUTPUT
        # TODO: DISREGARDS ILLEGAL LEVELS/SHINY/POKEMON ETC ETC

        #Check formID
        if( False ):
            return None
        p = pb.pokemon(pokemonChild.formID) #Get the pokemon to reference

        #Check gender
        gr = p.species.gender_rate
        if( gr == -1 and pokemonChild.gender != pb.gender("genderless").id ):
            return None #TODO: HAVEN'T TESTED WRITE UNIT TESTS
        if( gr != -1 and pokemonChild.gender == pb.gender("genderless").id ):
            return None
        if( gr == 0 and pokemonChild.gender != pb.gender("male").id ):
            return None #TODO: HAVEN'T TESTED WRITE UNIT TESTS
        if( gr == 8 and pokemonChild.gender != pb.gender("female").id ):
            return None #TODO: HAVEN'T TESTED WRITE UNIT TESTS

        #Check itemID
        if( self.validateItemID(pokemonChild.itemID) == None ):
            return None

        #Check ability
        abilityValid = False
        for i in range(0, len(p.abilities)):
            if( p.abilities[i].slot == pokemonChild.ability ):
                abilityValid = True
        if( abilityValid == False ):
            return None

        #Check level
        if( pokemonChild.level > constants.MAX_LEVEL or pokemonChild.level < constants.MIN_LEVEL ):
            return None

        #Check shiny
            #Shiny can't be invalid

        #Check happiness
        if( pokemonChild.happiness > constants.MAX_HAPPINESS or pokemonChild.happiness < constants.MIN_HAPPINESS ):
            return None

        #Check natureID
        if( pokemonChild.natureID > constants.MAX_NATUREID or pokemonChild.natureID < constants.MIN_NATUREID ):
            return None

        #Check EVs
            #Check total
        if( pokemonChild.evHP + pokemonChild.evAtk + pokemonChild.evDef + pokemonChild.evSpA + pokemonChild.evSpD + pokemonChild.evSpe > constants.MAX_EV_TOTAL ):
            return None
        # Create an array for all the EVs and itterate checks over it
        childEVs = [pokemonChild.evHP, pokemonChild.evAtk, pokemonChild.evDef, pokemonChild.evSpA, pokemonChild.evSpD, pokemonChild.evSpe]
        for i in range(0, len(childEVs)):
            if( childEVs[i] > constants.MAX_EV or childEVs[i] < constants.MIN_EV ):
                return None

        #Check IVs
        childIVs = [pokemonChild.ivHP, pokemonChild.ivAtk, pokemonChild.ivDef, pokemonChild.ivSpA, pokemonChild.ivSpD, pokemonChild.ivSpe]
        for i in range(0, len(childIVs)):
            if( childIVs[i] > constants.MAX_IV or childIVs[i] < constants.MIN_IV ):
                return None

        #Check Moves
        if( self.validateMoves(pokemonChild) == None ):
            return None

        return pokemonChild

    def validateMoves(self, pc):
        moves = [pc.move1, pc.move2, pc.move3, pc.move4]
        p = pb.pokemon(pc.formID) #Get the pokemon to reference
        for x in range(0, constants.MAX_MOVES):
            if( moves[x] != None ):
                inMoveList = False
                for i in range(0, len(p.moves)):
                    if( moves[x] == p.moves[i].move.id ):
                        inMoveList = True
                if( inMoveList == False ):
                    return None

        # Check for no moves
        if( pc.move1 == None and pc.move2 == None and pc.move3 == None and pc.move4 == None):
            return None

        # Check for move duplication #TODO: CLEAN THIS MESS UP
        if( pc.move1 != None and (pc.move1 == pc.move2 or pc.move1 == pc.move3 or pc.move1 == pc.move4) ):
            return None
        if( pc.move2 != None and (pc.move2 == pc.move3 or pc.move2 == pc.move4) ):
            return None
        if( pc.move3 != None and (pc.move3 == pc.move4) ):
            return None

        return pc

    def validateItemID(self, itemID):
        # Check validiity of the item
        invalidItem = False
        #Check its an item in the database
        try:
            item = pb.item(itemID)
            # Check if item is holdable
            holdableItem = False
            for i in range(0, len(item.attributes)):
                if( item.attributes[i].id == pb.item_attribute("holdable").id ):
                    holdableItem = True
            if( holdableItem == False ):
                print("Item not holdable") #DEBUG
                invalidItem = True
        except ValueError:
            print("Item not in database") #DEBUG
            invalidItem = True

        if( invalidItem == False ):
            print("Item Valid") #DEBUG
            return itemID
        else:
            print("Item Invalid") #DEBUG
            return None

    def populationReplacement(self, population, fitness, child, childFitness, populationSize):
        #Random Replacement but only if child is better than previous member

        indexToChange = random.randrange(populationSize)
        if( fitness[indexToChange] > childFitness ):
            population[indexToChange] = child
            fitness[indexToChange] = childFitness
        return population, fitness
