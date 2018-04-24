import pokebase as pb

class pokemonIndividual:

    genderDictionary = {pb.gender("female").id: "(F) ",
                        pb.gender("male").id: "(M) ",
                        pb.gender("genderless").id: ""}

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
        return self.showdownFormat()

    def getAbility(self):
        abilities = pb.pokemon(self.formID).abilities
        for i in range(0, len(abilities)):
            if( abilities[i].slot == self.ability):
                return abilities[i].ability

    def showdownFormat(self):
        s = str(pb.pokemon(self.formID)) + " "
        s += self.genderDictionary[self.gender]
        if( self.itemID != None):
            s += "@ " + pb.item(self.itemID).name
        s += "\n"
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
        #Title to make nature capitalised so showdown accepts it
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
