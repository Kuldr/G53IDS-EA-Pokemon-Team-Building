import pokebase as pb
from enum import Enum

class GENDER(Enum):
    MALE = 1
    FEMALE = 2
    GENDERLESS = 3

class pokemon:

    #TODO: Hardcoded values deal with it
    genderDictionary = {GENDER.MALE: "(M) ",
                        GENDER.FEMALE: "(F) ",
                        GENDER.GENDERLESS: ""}
    natureDictionary = {}

    def __init__(self):
        self.level = 51

    #TODO: GET THIS WORKING IN THE INTERPRETER SO I CAN WRITE THE SHOWDOWN FORMAT
    #TODO: ACCESS OF VARIABLES; DO YOU MAKE SURE YOU CAN'T GET THINGS LIKE LEVEL OVER 100 ??
    #TODO: WRITE BETTER COMMENTS

    #Class Variables
    formID = 25 #Pikachu #Stored as the form id from which other infomation can be derived
    gender = GENDER.FEMALE #Stored as Enum
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

    #Methods
    def __str__(self):
        return self.showdownFormat

    def getAbility(self):
        abilities = pb.pokemon(self.formID).abilities
        for i in range(0, len(abilities)):
            if( abilities[i].slot == self.ability):
                return abilities[i].ability

    def showdownFormat(self):
        s = str(pb.pokemon(self.formID)) + " "
        s += self.genderDictionary[self.gender]
        s += "@ " + pb.item(self.itemID).name + "\n" #TODO
        s += "Ability: " + self.getAbility().name + "\n"
        s += "Level: " + str(self.level) + "\n"
        if( self.shiny == True ):
            s += "Shiny: Yes\n"
        s += "Happiness: " + str(self.happiness) + "\n"
        s += "EVs: "
        s += str(self.evHP) + " HP / "
        s += str(self.evAtk) + " Atk / "
        s += str(self.evDef) + " Def / "
        s += str(self.evSpA) + " SpA / "
        s += str(self.evSpD) + " SpD / "
        s += str(self.evSpe) + " Spe\n"
        s += pb.nature(self.natureID).name.title() + " Nature\n"
        #TODO title to make nature capitalised so showdown accepts it
        s += "IVs: "
        s += str(self.ivHP) + " HP / "
        s += str(self.ivAtk) + " Atk / "
        s += str(self.ivDef) + " Def / "
        s += str(self.ivSpA) + " SpA / "
        s += str(self.ivSpD) + " SpD / "
        s += str(self.ivSpe) + " Spe\n"
        #MOVES
        if( self.move1 != None ):
            s += "- " + pb.move(self.move1).name + "\n"
        if( self.move2 != None ):
            s += "- " + pb.move(self.move2).name + "\n"
        if( self.move3 != None ):
            s += "- " + pb.move(self.move3).name + "\n"
        if( self.move4 != None ):
            s += "- " + pb.move(self.move4).name + "\n"
        return s

p = pokemon()
print(p.showdownFormat())

# Previously created strings for the showdownFormat
#     def strFormName(self):
#         return str(pb.pokemon(self.formID)) + " "
#
#     def strGender(self):
#         dictionary = {GENDER.MALE: "(M) ", GENDER.FEMALE: "(F) ", GENDER.GENDERLESS: ""}
#         return dictionary[self.gender]
#
#     def strItem(self):
#         return pb.item(self.itemID).name
#
#     def strAbility(self, ability):
#         return ability.name
#
#     def strLevel(self):
#         return str(self.level)
#
#     def strShiny(self):
#         if( self.shiny == True ):
#             return "Shiny: Yes\n"
#         else:
#             return ""
#
#     def strHappiness(self):
#         return str(self.happiness)
#
#     def strEvs(self):
#         s = "EVs: "
#         s = s + str(self.evHP) + " HP / "
#         s = s + str(self.evAtk) + " Atk / "
#         s = s + str(self.evDef) + " Def / "
#         s = s + str(self.evSpA) + " SpA / "
#         s = s + str(self.evSpD) + " SpD / "
#         s = s + str(self.evSpe) + " Spe\n"
#         return s
#
#     def strNature(self):
#         return self.nature + " Nature\n"
#
#     def strIVs(self):
#         s = "IVs: "
#         s = s + str(self.ivHP) + " HP / "
#         s = s + str(self.ivAtk) + " Atk / "
#         s = s + str(self.ivDef) + " Def / "
#         s = s + str(self.ivSpA) + " SpA / "
#         s = s + str(self.ivSpD) + " SpD / "
#         s = s + str(self.ivSpe) + " Spe\n"
#         return s
#
#     def strMoves(self):
#         s = "- " + self.move1 + "\n"
#         s = s + "- " + self.move2 + "\n"
#         s = s + "- " + self.move3 + "\n"
#         s = s + "- " + self.move4
#         return s
