import pokebase as pb

POKEMON_SPECIES_ID = 133
POKEMON_ABILITY_SLOT = 3

# POKEMON_SPECIES_ID is the species ID of the individual
# POKRMON_ABILITY_SLOT is the slot of the ability to find
pokemon = pb.pokemon(POKEMON_SPECIES_ID)
abilities = pokemon.abilities
ability = None
for i in range(len(abilities)):
    if( abilities[i].slot == POKEMON_ABILITY_SLOT ):
        ability = abilities[i].ability
# The ability of the individual is now stored in ability

print(ability)
