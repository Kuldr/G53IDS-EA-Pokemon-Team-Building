import constants
import random
import math
import pokebase as pb
from pokemonTeamIndividual import pokemonTeamIndividual
from pokemonIndividual import pokemonIndividual

class problemHelper:

    def initialisePokemonIndividual():
        #TODO: First made it to just make a pokemon not bothered about validation
        #TODO Need to make somethings be able to be None - This can be a variable in the constants file

        # Generates the default form and later on checks for other forms
        formID = random.randrange(constants.MIN_FORMID, constants.MAX_FORMID+1)

        # Write the item as teneray opperators like pokemon generation
        itemID = None if random.random() <= constants.NO_HELD_ITEM_RATE else problemHelper.initialiseItem()

        level = random.randrange(constants.MIN_LEVEL, constants.MAX_LEVEL+1)
        shiny = random.choice([True, False])
        happiness = random.randrange(constants.MIN_HAPPINESS, constants.MAX_HAPPINESS+1)
        natureID = random.randrange(constants.MIN_NATUREID, constants.MAX_NATUREID+1)
        ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe = problemHelper.initialiseIVs()

        #Initialise EVs to Minumum ev value
        #TODO: DOES IT MATTER THAT THIS GIVES OUT ALL OF THE EVs
        #TODO: DOES IT MATTER THAT THE EV SPREAD WILL BE ~85 for all stats
        #TODO: COULD GENERATE 4 AT A TIME AS THAT IS ALL THAT MATTERS (508)
        #TODO: NEED TO VALIDATE THAT YOU DON'T HAVE ANY STAT OVER 256
        evHP, evAtk, evDef, evSpA, evSpD, evSpe = problemHelper.initialiesEVs()

        #Pokemon dependant info so references the pokemon to get relevant info
        formVarieties = pb.pokemon(formID).species.varieties
        formRand = random.randrange(0, len(formVarieties))
        formID = formVarieties[formRand].pokemon.id # Update the formID into new form
        #TODO: CHECK IF FORM IS VALID IN BATTLE
        # pb.pokemon(formID).forms[0].is_battle.only
        # Mimikyu forms like disguised and totem come to mind

        p = pb.pokemon(formID) #Get the pokemon to reference

        #Randomly generate an ability slot
        ability = problemHelper.initialiseAbility(p)

        #Randomly generates a gender but at the correct ratio
        gender = problemHelper.initialiseGender(p)

        # TODO: ?? Make move indexing some kind of list for generation and Validation
        # This could also make it so that checking for dupes is easier
        move1, move2, move3, move4 = problemHelper.initialiseMoves(p)

        #Check and remove move duplication
        if( move1 == move2 or move1 == move3 or move1 == move4 ):
            # print("Duplicate Move") #DEBUG
            move1 = None
        if( move2 == move3 or move2 == move4 ):
            # print("Duplicate Move") #DEBUG
            move2 = None
        if( move3== move4 ):
            # print("Duplicate Move") #DEBUG
            move3 = None

        # Check for no moves
        if( move1 == None and move2 == None and move3 == None and move4 == None):
            move1 = p.moves[random.randrange(0, len(p.moves))].move.id

        return pokemonIndividual(formID, gender, itemID, ability, level, shiny,
                                    happiness, natureID,
                                    evHP, evAtk, evDef, evSpA, evSpD, evSpe,
                                    ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe,
                                    move1, move2, move3, move4)

    def initialiseAbility(pbPokemon):
        abilityIndex = random.randrange(0, len(pbPokemon.abilities)) #Gives a random number to index the abilities
        ability = pbPokemon.abilities[abilityIndex].slot #Gets the slot number for that ability index
        return ability

    def initialiseGender(pbPokemon):
        gr = pbPokemon.species.gender_rate #Gender Rate is given as x, where x/8 gives the chance of being female unless x = -1 where then the pokemon is genderless
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
        return gender

    def initialiseMoves(pbPokemon):
        moves = []
        for i in range(0, constants.NUMBER_OF_MOVES):
            moves.append(None if random.random() <= constants.NO_MOVE_RATE else pbPokemon.moves[random.randrange(0, len(pbPokemon.moves))].move.id)
        return moves[0], moves[1], moves[2], moves[3]

    def initialiseIVs():
        IVs = []
        for i in range(0, constants.NUMBER_OF_STATS):
            IVs.append(random.randrange(constants.MIN_IV, constants.MAX_IV+1))
        return IVs[0], IVs[1], IVs[2], IVs[3], IVs[4], IVs[5]

    def initialiesEVs():
        # Randomly distribute EVs 1 by 1
        EVs = [constants.MIN_EV]*constants.NUMBER_OF_STATS
        for _ in range(0, constants.MAX_EV_TOTAL):
            r = random.randrange(0, constants.NUMBER_OF_STATS)
            EVs[r] +=1
        return EVs[0], EVs[1], EVs[2], EVs[3], EVs[4], EVs[5]

    def initialiseItem():
        itemID = random.randrange(constants.MIN_ITEMID, constants.MAX_ITEMID+1)
        while problemHelper.validateItemID(itemID) == None:
            itemID = random.randrange(constants.MIN_ITEMID, constants.MAX_ITEMID+1)
        return itemID

    def validatePokemonIndividual(pokemonChild):
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
            return None
        if( gr != -1 and pokemonChild.gender == pb.gender("genderless").id ):
            return None
        if( gr == 0 and pokemonChild.gender != pb.gender("male").id ):
            return None
        if( gr == 8 and pokemonChild.gender != pb.gender("female").id ):
            return None

        #Check itemID
        if( problemHelper.validateItemID(pokemonChild.itemID) == None ):
            return None

        #Check ability
        abilityValid = False
        for i in range(0, len(p.abilities)):
            if( p.abilities[i].slot == pokemonChild.ability ):
                abilityValid = True
        if( abilityValid == False ):
            return None

        #Check level
        if( pokemonChild.level > constants.MAX_LEVEL):
            return None
        if( pokemonChild.level < constants.MIN_LEVEL ):  
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
        if( problemHelper.validateMoves(pokemonChild) == None ):
            return None

        return pokemonChild

    def validateMoves(pc):
        moves = [pc.move1, pc.move2, pc.move3, pc.move4]
        p = pb.pokemon(pc.formID) #Get the pokemon to reference
        for x in range(0, constants.NUMBER_OF_MOVES):
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

    def validateItemID(itemID):
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
                # print("Item not holdable") #DEBUG
                invalidItem = True
        except ValueError:
            # print("Item not in database") #DEBUG
            invalidItem = True

        if( invalidItem == False ):
            # print("Item Valid") #DEBUG
            return itemID
        else:
            # print("Item Invalid") #DEBUG
            return None

    def teamVTeam(team1, team2):
        # Returns number of wins for team1 against team2
        print("\t\t\tScoring Pokemon 1")
        print("\t\t\t", end='', flush=True)
        score = problemHelper.pokemonVTeam(team1.pokemon1, team2)
        print("\t\t\tScoring Pokemon 2")
        print("\t\t\t", end='', flush=True)
        score += problemHelper.pokemonVTeam(team1.pokemon2, team2)
        print("\t\t\tScoring Pokemon 3")
        print("\t\t\t", end='', flush=True)
        score += problemHelper.pokemonVTeam(team1.pokemon3, team2)
        print("\t\t\tScoring Pokemon 4")
        print("\t\t\t", end='', flush=True)
        score += problemHelper.pokemonVTeam(team1.pokemon4, team2)
        print("\t\t\tScoring Pokemon 5")
        print("\t\t\t", end='', flush=True)
        score += problemHelper.pokemonVTeam(team1.pokemon5, team2)
        print("\t\t\tScoring Pokemon 6")
        print("\t\t\t", end='', flush=True)
        score += problemHelper.pokemonVTeam(team1.pokemon6, team2)
        print("\tTeam Score = " + str(score))
        return score

    def pokemonVTeam(pokemon1, team2):
        # Returns number of wins for pokemon1 against team2
        score = problemHelper.pokemonVPokemon(pokemon1, team2.pokemon1)
        score += problemHelper.pokemonVPokemon(pokemon1, team2.pokemon2)
        score += problemHelper.pokemonVPokemon(pokemon1, team2.pokemon3)
        score += problemHelper.pokemonVPokemon(pokemon1, team2.pokemon4)
        score += problemHelper.pokemonVPokemon(pokemon1, team2.pokemon5)
        score += problemHelper.pokemonVPokemon(pokemon1, team2.pokemon6)
        print("Score = " + str(score))
        return score

    def pokemonVPokemon(pokemon1, pokemon2):
        # Returns 1 if pokemon1 wins, 0 if they lose

        #Check if either pokemon are none
        if( pokemon1 == None ):
            return 0
        if( pokemon2 == None ):
            return 1

        #TODO What if a move is None
        pokemon1Moves = [pokemon1.move1, pokemon1.move2, pokemon1.move3, pokemon1.move4]
        pokemon2Moves = [pokemon2.move1, pokemon2.move2, pokemon2.move3, pokemon2.move4]
        pokemon1MovePower = [0, 0, 0, 0]
        pokemon2MovePower = [0, 0, 0, 0]
        # Get the base power for each move including STAB and Type Advantage
        for i in range(0, len(pokemon1Moves)):
            if( pokemon1Moves[i] != None ):
                pokemon1MovePower[i] = problemHelper.pokemonMovePower(pokemon1Moves[i], pokemon1, pokemon2)
            else:
                pokemon1MovePower[i] = 0
        for i in range(0, len(pokemon2Moves)):
            if( pokemon2Moves[i] != None ):
                pokemon2MovePower[i] = problemHelper.pokemonMovePower(pokemon2Moves[i], pokemon2, pokemon1)
            else:
                pokemon2MovePower[i] = 0
        # Get the Stats for each pokemon
        pokemon1Stats = problemHelper.pokemonStats(pokemon1)
        pokemon2Stats = problemHelper.pokemonStats(pokemon2)
        # Calculate the damage each move will do
        pokemon1MoveDamage = [0, 0, 0, 0]
        pokemon2MoveDamage = [0, 0, 0, 0]
        for i in range(0, len(pokemon1Moves)):
            if( pokemon1Moves[i] != None ):
                # Get the type of the move
                damageClass = pb.move(pokemon1Moves[i]).damage_class.id
                # If Physical attack
                if( damageClass == pb.move_damage_class("physical").id ):
                    pokemon1MoveDamage[i] = problemHelper.damageDealt(pokemon1.level, pokemon1MovePower[i], pokemon1Stats[1], pokemon2Stats[2], 1)
                # If Special attack
                elif( damageClass == pb.move_damage_class("special").id ):
                    pokemon1MoveDamage[i] = problemHelper.damageDealt(pokemon1.level, pokemon1MovePower[i], pokemon1Stats[3], pokemon2Stats[4], 1)
                # If Status Move
                elif( damageClass == pb.move_damage_class("status").id ):
                    pokemon1MoveDamage[i] = 0
            else:
                pokemon1MoveDamage[i] = 0
        for i in range(0, len(pokemon2Moves)):
            if( pokemon2Moves[i] != None ):
                # Get the type of the move
                damageClass = pb.move(pokemon2Moves[i]).damage_class.id
                # If Physical attack
                if( damageClass == pb.move_damage_class("physical").id ):
                    pokemon2MoveDamage[i] = problemHelper.damageDealt(pokemon2.level, pokemon2MovePower[i], pokemon2Stats[1], pokemon1Stats[2], 1)
                # If Special attack
                elif( damageClass == pb.move_damage_class("special").id ):
                    pokemon2MoveDamage[i] = problemHelper.damageDealt(pokemon2.level, pokemon2MovePower[i], pokemon2Stats[3], pokemon1Stats[4], 1)
                # If Status Move
                elif( damageClass == pb.move_damage_class("status").id ):
                    pokemon2MoveDamage[i] = 0
            else:
                pokemon2MoveDamage[i] = 0

        # TODO: Improve this

        # print(pokemon1MoveDamage) #DEBUG
        # print(pokemon2MoveDamage) #DEBUG

        #If Pokemon 1 does more damage return true
        if( max(pokemon1MoveDamage) >= max(pokemon2MoveDamage) ):
            print("Win,  ", end='', flush=True)
            return 1
        else:
            print("Loss, ", end='', flush=True)
            return 0

    def damageDealt(level, power, attack, defense, modifiers):
        return (((((2 * level)/5)+2)*power*(attack/defense)/50)+2)*modifiers

    def pokemonStats(pokemon):
        #[hp, atk, defense, spa, spd, spe] = [0, 0, 0, 0, 0, 0]
        # Get the pokemon base stats
        baseStats = pb.pokemon(pokemon.formID).stats
        natureModifiers = [1, 1, 1, 1, 1]
        incStat = pb.nature(pokemon.natureID).increased_stat
        decStat = pb.nature(pokemon.natureID).decreased_stat
        if( incStat != None):
            # TODO: Clean up by changing to a dictionary
            if( incStat.id == pb.stat("attack").id ):
                natureModifiers[0] = 1.1
            elif( incStat.id == pb.stat("defense").id ):
                natureModifiers[1] = 1.1
            elif( incStat.id == pb.stat("special-attack").id ):
                natureModifiers[2] = 1.1
            elif( incStat.id == pb.stat("special-defense").id ):
                natureModifiers[3] = 1.1
            elif( incStat.id == pb.stat("speed").id ):
                natureModifiers[4] = 1.1
        if( decStat != None):
            if( decStat.id == pb.stat("attack").id ):
                natureModifiers[0] = 0.9
            elif( decStat.id == pb.stat("defense").id ):
                natureModifiers[1] = 0.9
            elif( decStat.id == pb.stat("special-attack").id ):
                natureModifiers[2] = 0.9
            elif( decStat.id == pb.stat("special-defense").id ):
                natureModifiers[3] = 0.9
            elif( decStat.id == pb.stat("speed").id ):
                natureModifiers[4] = 0.9
        # Calculate each stat
        hp = problemHelper.pokemonHP(baseStats[5].base_stat, pokemon.ivHP, pokemon.evHP, pokemon.level)
        atk = problemHelper.pokemonStat(baseStats[4].base_stat, pokemon.ivAtk, pokemon.evAtk, pokemon.level, natureModifiers[0])
        defense = problemHelper.pokemonStat(baseStats[3].base_stat, pokemon.ivDef, pokemon.evDef, pokemon.level, natureModifiers[1])
        spa = problemHelper.pokemonStat(baseStats[2].base_stat, pokemon.ivSpA, pokemon.evSpA, pokemon.level, natureModifiers[2])
        spd = problemHelper.pokemonStat(baseStats[1].base_stat, pokemon.ivSpD, pokemon.evSpD, pokemon.level, natureModifiers[3])
        spe = problemHelper.pokemonStat(baseStats[0].base_stat, pokemon.ivSpe, pokemon.evSpe, pokemon.level, natureModifiers[4])
        return [hp, atk, defense, spa, spd, spe]

    def pokemonHP(base, iv, ev, level):
        innerBracket = (2 * base + iv + math.floor(ev/4))
        innerBracket *= level
        floor = math.floor(innerBracket/100)
        return floor + level + 10

    def pokemonStat(base, iv, ev, level, natureModifier):
        innerBracket = (2 * base + iv + math.floor(ev/4))
        innerBracket *= level
        floor = math.floor(innerBracket/100)
        floor += 5
        return math.floor(floor * natureModifier)

    def pokemonMovePower(move, pokemonAtk, pokemonDef):
        if( move == None ):
            return 0
        elif( pb.move(move).damage_class.id == pb.move_damage_class(1).id ):
            return 0
        else:
            # Set the base power
            moveBasePower = pb.move(move).power
            # If the move has variable power its base power is None
            if( moveBasePower == None ):
                return 0
            #Get Move Type
            moveType = pb.move(move).type
            # Apply STAB
            pokemonAtkTypes = pb.pokemon(pokemonAtk.formID).types
            for j in range(0, len(pokemonAtkTypes)):
                if( moveType.id == pokemonAtkTypes[j].type.id ):
                    moveBasePower *= 1.5
            # Check for Weakness/Resistance against each type
            pokemonDefTypes = pb.pokemon(pokemonDef.formID).types
            for j in range(0, len(pokemonDefTypes)):
                #Check Move effectivness against the opponent type
                #No Effect
                noDamageTo = moveType.damage_relations.no_damage_to
                for k in range(0, len(noDamageTo)):
                    if( noDamageTo[k]['name'] == pokemonDefTypes[j].type.name ):
                        moveBasePower *= 0
                #Half Damage
                halfDamageTo = moveType.damage_relations.half_damage_to
                for k in range(0, len(halfDamageTo)):
                    if( halfDamageTo[k]['name'] == pokemonDefTypes[j].type.name ):
                        moveBasePower *= 0.5
                #Double Damage
                doubleDamageTo = moveType.damage_relations.double_damage_to
                for k in range(0, len(doubleDamageTo)):
                    if( doubleDamageTo[k]['name'] == pokemonDefTypes[j].type.name ):
                        moveBasePower *= 2
            #Return the final base power
            return moveBasePower

    def changeIVS(pokemon, ivChange):
        #Check the pokemn isn't null
        if( pokemon == None ):
            return pokemon

        if( pokemon.ivHP + ivChange > constants.MAX_IV ):
            pokemon.ivHP = constants.MAX_IV
        elif( pokemon.ivHP + ivChange < constants.MIN_IV ):
            pokemon.ivHP = constants.MIN_IV
        else:
            pokemon.ivHP  += ivChange

        if( pokemon.ivAtk + ivChange > constants.MAX_IV ):
            pokemon.ivAtk = constants.MAX_IV
        elif( pokemon.ivAtk + ivChange < constants.MIN_IV ):
            pokemon.ivAtk = constants.MIN_IV
        else:
            pokemon.ivAtk  += ivChange

        if( pokemon.ivDef + ivChange > constants.MAX_IV ):
            pokemon.ivDef = constants.MAX_IV
        elif( pokemon.ivDef + ivChange < constants.MIN_IV ):
            pokemon.ivDef = constants.MIN_IV
        else:
            pokemon.ivDef  += ivChange

        if( pokemon.ivSpA + ivChange > constants.MAX_IV ):
            pokemon.ivSpA = constants.MAX_IV
        elif( pokemon.ivSpA + ivChange < constants.MIN_IV ):
            pokemon.ivSpA = constants.MIN_IV
        else:
            pokemon.ivSpA  += ivChange

        if( pokemon.ivSpD + ivChange > constants.MAX_IV ):
            pokemon.ivSpD = constants.MAX_IV
        elif( pokemon.ivSpD + ivChange < constants.MIN_IV ):
            pokemon.ivSpD = constants.MIN_IV
        else:
            pokemon.ivSpD  += ivChange

        if( pokemon.ivSpe + ivChange > constants.MAX_IV ):
            pokemon.ivSpe = constants.MAX_IV
        elif( pokemon.ivSpe + ivChange < constants.MIN_IV ):
            pokemon.ivSpe = constants.MIN_IV
        else:
            pokemon.ivSpe += ivChange

        return pokemon
