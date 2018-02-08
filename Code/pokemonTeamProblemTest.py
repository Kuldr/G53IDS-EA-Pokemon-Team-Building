from pokemonTeamProblem import pokemonTeamProblem
from pokemonTeamIndividual import pokemonTeamIndividual
import testPokemon

problem = pokemonTeamProblem()

# # Test Initialisation (NOTE NOT FULL ON TESTS)
# t = problem.initialiseIndividual()
# t = problem.validation(t)
# print(str(t))

# # Test validation
# p = testPokemon.p
# t = pokemonTeamIndividual(p, p, p, p, p, p)
# ans = problem.validation(t)
# print(ans)

# Test Mutation
p = testPokemon.p
t = pokemonTeamIndividual(p, None, None, None, None, None)
print(t)
t_ = problem.mutation(t, 1)
print(t_)
