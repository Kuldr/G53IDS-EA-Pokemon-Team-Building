import pokebase as pb
from enum import Enum

class GENDER(Enum):
    MALE = 1
    FEMALE = 2
    GENDERLESS = 3

class pokemon:

    def __init__(self):
        self.level = 51

    #TODO: GET THIS WORKING IN THE INTERPRETER SO I CAN WRITE THE SHOWDOWN FORMAT
    #TODO: ACCESS OF VARIABLES; DO YOU MAKE SURE YOU CAN'T GET THINGS LIKE LEVEL OVER 100 ??
    #TODO: WRITE BETTER COMMENTS

    #Class Variables
    formID = 25 #Pikachu #Stored as the form id from which other infomation can be derived
    gender = GENDER.GENDERLESS #Stored as Enum
    item = 213 #Light Ball #Stored as item id
    ability = 3 #Lightning Rod #Stored as the ability slot of that pokemon, to get further information on the ability would need to get all of the pokemons abilities and then iterate over them until the slot number matches
    level = 51 #Stored as an int
    shiny = True #Do I need #TODO
    happiness = 249 #Stored as an int

    nature = "Mild" #Convert to enum #TODO

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

    #TODO MOVES
    move1 = "Discharge" #Convert to ids
    move2 = "Extreme Speed"
    move3 = "Fake Out"
    move4 = "Hidden Power [Fire]"

    #Methods
    def __str__(self):
        return self.showdownFormat

    def strFormName(self):
        return str(pb.pokemon(self.formID))

    def strGender(self):
        dictionary = {GENDER.MALE: "(M) ", GENDER.FEMALE: "(F) ", GENDER.GENDERLESS: ""}
        return dictionary[self.gender]

    def strItem(self):
        return pb.item(self.item).name

    def strAbility(self, ability):
        return ability.name

    def getAbility(self):
        abilities = pb.pokemon(self.formID).abilities
        for i in range(0, len(abilities)):
            if( abilities[i].slot == self.ability):
                return abilities[i].ability

    def strLevel(self):
        return str(self.level)

    def strShiny(self):
        if( self.shiny == True ):
            return "Shiny: Yes\n"
        else:
            return ""

    def strHappiness(self):
        return str(self.happiness)

    def strEvs(self):
        s = "EVs: "
        s = s + str(self.evHP) + " HP / "
        s = s + str(self.evAtk) + " Atk / "
        s = s + str(self.evDef) + " Def / "
        s = s + str(self.evSpA) + " SpA / "
        s = s + str(self.evSpD) + " SpD / "
        s = s + str(self.evSpe) + " Spe\n"
        return s

    def strNature(self):
        return self.nature + " Nature\n"

    def strIVs(self):
        s = "IVs: "
        s = s + str(self.ivHP) + " HP / "
        s = s + str(self.ivAtk) + " Atk / "
        s = s + str(self.ivDef) + " Def / "
        s = s + str(self.ivSpA) + " SpA / "
        s = s + str(self.ivSpD) + " SpD / "
        s = s + str(self.ivSpe) + " Spe\n"
        return s

    def strMoves(self):
        #TODO: WHAT IF NOT 4 MOVES
        s = "- " + self.move1 + "\n"
        s = s + "- " + self.move2 + "\n"
        s = s + "- " + self.move3 + "\n"
        s = s + "- " + self.move4
        return s

    def showdownFormat(self):
        #TODO DO I MAKE THIS ONLY CALL ALL THE METHODS AND ADD NO EXTRA
        s = "" #Start a blank string and then add each part to it individually
        s = s + self.strFormName() + " "
        s = s + self.strGender()
        s = s + "@ " + self.strItem() + "\n"
        s = s + "Ability: " + self.strAbility(self.getAbility()) + "\n"
        s = s + "Level: " + self.strLevel() + "\n"
        s = s + self.strShiny()
        s = s + "Happiness: " + self.strHappiness() + "\n"
        s = s + self.strEvs()
        s = s + self.strNature()
        s = s + self.strIVs()
        s = s + self.strMoves()
        return s

p = pokemon()
print(p.showdownFormat())
