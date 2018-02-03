from Gender import Gender
from pokemonIndividual import pokemonIndividual

formID = 25 #Pikachu #Stored as the form id from which other infomation can be derived
gender = 1 #Female #Stored as gender id 
itemID = 213 #Light Ball #Stored as item id
ability = 3 #Lightning Rod #Stored as the ability slot of that pokemon, to get further information on the ability would need to get all of the pokemons abilities and then iterate over them until the slot number matches
level = 51 #Stored as an int
shiny = True #Do I need #TODO
happiness = 249 #Stored as an int

natureID = 8 #Mild #Stored as pokebase nature id

#EVs stored as ints for that value
evHP = 120
evAtk = 56
evDef = 148
evSpA = 88
evSpD = 52
evSpe = 44

#IVs stored as ints for that value
ivHP = 26
ivAtk = 30
ivDef = 27
ivSpA = 23
ivSpD = 25
ivSpe = 28

#MOVES
#TODO: Hidden Power it won't calculate the type :/
move1 = 435 #"Discharge" #Convert to ids (None for no move)
move2 = 245 #"Extreme Speed"
move3 = 252 #"Fake Out"
move4 = 237 #"Hidden Power" Actually HP Fire

p = pokemonIndividual(formID, gender, itemID, ability, level, shiny,
                happiness, natureID,
                evHP, evAtk, evDef, evSpA, evSpD, evSpe,
                ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe,
                move1, move2, move3, move4)
#print(p.showdownFormat())
