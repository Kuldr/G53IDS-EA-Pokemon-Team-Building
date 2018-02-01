from pokemonTeamProblem import pokemonTeamProblem
from pokemonTeamIndividual import pokemonTeamIndividual

problem = pokemonTeamProblem()
t = problem.initialiseIndividual()
print(t.teamShowdownFormat())
