import pokebase as pb

chesto = pb.NamedAPIResource('berry', 'chesto')
print(chesto.name)
print(chesto.natural_gift_type.name)

charmander = pb.pokemon('charmander')
print(charmander.height)
print(charmander.abilities[1])

bulba = pb.pokemon_sprite(1)           # And sprites too!
print(bulba.path)
