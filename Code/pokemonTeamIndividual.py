import pokemonIndividual

class pokemonTeamIndividual:

    def __init__(self, pokemon1, pokemon2, pokemon3,
                    pokemon4, pokemon5, pokemon6):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5
        self.pokemon6 = pokemon6

    def __str__(self):
        return self.teamShowdownFormat

    def teamShowdownFormat(self):
        s = str(self.pokemon1) + "\n"
        s += str(self.pokemon2) + "\n"
        s += str(self.pokemon3) + "\n"
        s += str(self.pokemon4) + "\n"
        s += str(self.pokemon5) + "\n"
        s += str(self.pokemon6) + "\n"
        return s
