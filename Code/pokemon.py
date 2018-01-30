import pokebase as pb

class pokemon:

    def __init__(self):
        self.level = 51

    #TODO: GET THIS WORKING IN THE INTERPRETER SO I CAN WRITE THE SHOWDOWN FORMAT
    #TODO: ACCESS OF VARIABLES; DO YOU MAKE SURE YOU CAN'T GET THINGS LIKE LEVEL OVER 100 ??
    #TODO: WRITE BETTER COMMENTS

    #Class Variables
    formID = 25 #Pikachu #Stored as the form id from which other infomation can be derived
    gender = "M" #Conver to enum #TODO
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

    def showdownFormat(self):
        #TODO ADDS IN A LINE ?? BETWEEN HAPPINESS AND EVS WHICH PREVENTS IMPORT
        s = "" #Start a blank string and then add each part to it individually
        s = s + str(pb.pokemon(self.formID)) + " "
        s = s + "(" + self.gender + ")" + " "
        s = s + "@ " + pb.item(self.item).name + "\n"
        s = s + "Ability: " + "Lightning Rod" + "\n" #TODO: GET THE ABILITY FROM THE SLOT, MAKE A METHOD FOR THIS PORBABLY
        s = s + "Level: " + str(self.level) + "\n"
        if( self.shiny == True ):
            s = s + "Shiny: Yes\n"
        s = s + "Happiness: " + str(self.happiness) + "\n"
        s = s + "EVs: "
        s = s + str(self.evHP) + " HP / "
        s = s + str(self.evAtk) + " Atk / "
        s = s + str(self.evDef) + " Def / "
        s = s + str(self.evSpA) + " SpA / "
        s = s + str(self.evSpD) + " SpD / "
        s = s + str(self.evSpe) + " Spe\n"
        s = s + self.nature + " Nature\n"
        s = s + "IVs: "
        s = s + str(self.ivHP) + " HP / "
        s = s + str(self.ivAtk) + " Atk / "
        s = s + str(self.ivDef) + " Def / "
        s = s + str(self.ivSpA) + " SpA / "
        s = s + str(self.ivSpD) + " SpD / "
        s = s + str(self.ivSpe) + " Spe\n"
        #TODO: WHAT IF NOT 4 MOVES
        s = s + "- " + self.move1 + "\n"
        s = s + "- " + self.move2 + "\n"
        s = s + "- " + self.move3 + "\n"
        s = s + "- " + self.move4
        return s

p = pokemon()
print(p.showdownFormat())
