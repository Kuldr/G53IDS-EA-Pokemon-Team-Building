#TODO: GET THIS WORKING IN THE INTERPRETER SO I CAN WRITE THE SHOWDOWN FORMAT
#TODO: ACCESS OF VARIABLES; DO YOU MAKE SURE YOU CAN'T GET THINGS LIKE LEVEL OVER 100 ??
#TODO: WRITE BETTER COMMENTS

import pokebase as pb
from Gender import Gender

class pokemonIndividual:

    #TODO: Hardcoded values deal with it
    genderDictionary = {Gender.MALE: "(M) ",
                        Gender.FEMALE: "(F) ",
                        Gender.GENDERLESS: ""}

    def __init__(self, formID, gender, itemID, ability, level, shiny,
                    happiness, natureID,
                    evHP, evAtk, evDef, evSpA, evSpD, evSpe,
                    ivHP, ivAtk, ivDef, ivSpA, ivSpD, ivSpe,
                    move1, move2, move3, move4):
        self.formID = formID
        self.gender = gender
        self.itemID = itemID
        self.ability = ability
        self.level = level
        self.shiny = shiny
        self.happiness = happiness
        self.natureID = natureID
        self.evHP = evHP
        self.evAtk = evAtk
        self.evDef = evDef
        self.evSpA = evSpA
        self.evSpD = evSpD
        self.evSpe = evSpe
        self.ivHP = ivHP
        self.ivAtk = ivAtk
        self.ivDef = ivDef
        self.ivSpA = ivSpA
        self.ivSpD = ivSpD
        self.ivSpe = ivSpe
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

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

# Previously created strings for the showdownFormat
#     def strFormName(self):
#         return str(pb.pokemon(self.formID)) + " "
#
#     def strGender(self):
#         dictionary = {Gender.MALE: "(M) ", Gender.FEMALE: "(F) ", Gender.GENDERLESS: ""}
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
