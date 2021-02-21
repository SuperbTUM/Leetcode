"""
GA with pyevolve. The challenge for GA in N-queens problem is to find all the possibilities.
Just a edgy thought
"""
from pyevolve import *
n = 6  # You can change n to any integer greater than zero
# I have problems in self-defined initialization
# if I want to define genes = [i for i in range(n)]
# Then I got an error, saying empty range for randrange() when calling CrossOvers in evolve function


def queens_eval(genes):
    collisions = 0
    for i in range(n):
        if i not in genes:
            return 0
    for i in range(n):
        col = False
        for j in range(n):
            if i != j and abs(i-j) == abs(genes[i] - genes[j]):
                col = True
                break
        if col:
            collisions += 1
    return n - collisions

def n_queens():
    genes = G1DList.G1DList(n)
    genes.setParams(rangemin=0, rangemax=n-1, bestrawscore=n)
    genes.initializator.set(Initializators.G1DListInitializatorInteger)
    genes.mutator.set(Mutators.G1DListMutatorSwap)
    genes.crossover.set(Crossovers.G1DListCrossoverCutCrossfill)
    genes.evaluator.set(queens_eval)

    ga = GSimpleGA.GSimpleGA(genes)
    ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
    ga.setMinimax(Consts.minimaxType["maximize"])

    ga.setPopulationSize(100)
    ga.setGenerations(1000)
    ga.setMutationRate(0.02)
    ga.setCrossoverRate(0.8)

    ga.evolve(freq_stats=10)
    best = ga.bestIndividual()
    print(best)

if __name__ == '__main__':
    n_queens()
