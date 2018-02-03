import constants
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

        # Generates the default form and later on checks for other forms

        while True:
            # Generate an item Max Item ID is 918
            itemID = random.randrange(0,918)+1

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
                break
        print("Item Generated") #DEBUG
        # Chance to make the Pokemon have no held item
        if( random.random() <= NO_HELD_ITEM_RATE ):
            itemID = None

        level = random.randrange(0, 100)+1
        shiny = random.choice([True, False]) #TODO: Shiny rate is way off and is it worth storing this value as it doesn't effect combat ??
        happiness = random.randrange(0, 256)
        natureID = random.randrange(0, 25)+1
        ivHP = random.randrange(0, 32)
        ivAtk = random.randrange(0, 32)
        ivDef = random.randrange(0, 32)
        ivSpA = random.randrange(0, 32)
        ivSpD = random.randrange(0, 32)
        ivSpe = random.randrange(0, 32)

        #Initialise EVs to 0
        evHP = 0
        evAtk = 0
        evDef = 0
        evSpA = 0
        evSpD = 0
        evSpe = 0
        # Randomly distribute EVs 1 by 1
        #TODO: DOES IT MATTER THAT THIS GIVES OUT ALL OF THE EVs
        #TODO: DOES IT MATTER THAT THE EV SPREAD WILL BE 85 for all stats
        #TODO: COULD GENERATE 4 AT A TIME AS THAT IS ALL THAT MATTERS (508)
        for _ in range(0, 510):
        #TODO: NEED TO VALIDATE THAT YOU DON'T HAVE ANY STAT OVER 256
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
        formVarieties = pb.pokemon(formID).sepcies.varieties
        formRand = random.randrange(0, len(formVarieties))
        formID = formVarieties[formRand].pokemon.id # Update the formID into new form

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

        moveIndex = random.randrange(0, len(p.moves))
        move1 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move2 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move3 = p.moves[moveIndex].move.id
        moveIndex = random.randrange(0, len(p.moves))
        move4 = p.moves[moveIndex].move.id

        # Chance to make the no move
        if( random.random() <= NO_MOVE_RATE ):
            move1 = None
        if( random.random() <= NO_MOVE_RATE ):
            move2 = None
        if( random.random() <= NO_MOVE_RATE ):
            move3 = None
        if( random.random() <= NO_MOVE_RATE ):
            move4 = None            

        #Check Move validity
        if( move1 == move2 or move1 == move3 or move1 == move4 ):
            print("Duplicate Move") #DEBUG
            move1 = None
        if( move2 == move3 or move2 == move4 ):
            print("Duplicate Move") #DEBUG
            move2 = None
        if( move3== move4 ):
            print("Duplicate Move") #DEBUG
            move3 = None

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
