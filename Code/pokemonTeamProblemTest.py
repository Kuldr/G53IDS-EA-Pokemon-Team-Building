from pokemonTeamProblem import pokemonTeamProblem
from pokemonTeamIndividual import pokemonTeamIndividual
import testPokemon

problem = pokemonTeamProblem()

# Test Initialisation (NOTE NOT FULL ON TESTS)
# t = problem.initialiseIndividual()
# print(str(t))

# Test validation
print("Sucess")
p = testPokemon.p
ans = problem.validation(p)
print(ans)

p.evSpD = -1

ans = problem.validation(p)
print(ans)
