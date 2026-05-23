import random
import math

#Gene

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.randint(0, 1)

    def mutate(self):
        self.value = 1 - self.value  # flip : 0→1 ou 1→0

    def __str__(self):
        return str(self.value)


#Chromosome

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:   # 1/2 chance de flip par gène
                gene.mutate()

    def is_perfect(self):
        return all(g.value == 1 for g in self.genes)

    def __str__(self):
        return "".join(str(g) for g in self.genes)


#DNA

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:   # 1/2 chance de muter par chromosome
                chromosome.mutate()

    def is_perfect(self):
        return all(c.is_perfect() for c in self.chromosomes)

    def score(self):
        return sum(g.value for c in self.chromosomes for g in c.genes)

    def __str__(self):
        return "\n".join(f"  Chr {i+1}: {c}" for i, c in enumerate(self.chromosomes))


# Organism — possède un DNA et un taux de mutation (environment)

class Organism:
    def __init__(self, dna, environment):
        self.dna         = dna
        self.environment = environment  # probabilité de muter

    def try_mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_perfect()

    def score(self):
        return self.dna.score()


# Simulation

NUM_ORGANISMS  = 10     # nombre d'organismes en parallèle
ENVIRONMENT    = 0.9    # probabilité de mutation par génération
MAX_GENERATIONS = 110_000

organisms = [Organism(DNA(), ENVIRONMENT) for _ in range(NUM_ORGANISMS)]

winner      = None
generations = 0

print("Simulation started...\n")

for generation in range(1, MAX_GENERATIONS + 1):
    generations = generation

    for organism in organisms:
        organism.try_mutate()

    # Cherche un organisme parfait (que des 1)
    for organism in organisms:
        if organism.is_perfect():
            winner = organism
            break

    if winner:
        break

    # Affiche la progression toutes les 1000 générations
    if generation % 1000 == 0:
        best = max(organisms, key=lambda o: o.score())
        print(f"  Gen {generation:>6} | Best score: {best.score()}/100")

# Résultats — Research Notebook

print("         BIOLOGY RESEARCH NOTEBOOK")

if winner:
    print(f"\nPerfect DNA found after {generations} generation(s)!\n")
    print("Winning DNA:")
    print(winner.dna)
    print(f"\n  Score      : {winner.score()}/100")
    print(f"  Organisms  : {NUM_ORGANISMS}")
    print(f"  Environment: {ENVIRONMENT} mutation rate")
else:
    print(f"\nNo perfect DNA found after {MAX_GENERATIONS} generations.")

print("CONCLUSION")
print(f"""
- With {NUM_ORGANISMS} organisms and a mutation rate of {ENVIRONMENT},
  a perfect DNA (100 genes all = 1) was reached in
  {generations} generation(s).

- Higher mutation rates → faster convergence but also
  more risk of destroying good genes already in place.

- Running multiple organisms in parallel drastically
  reduces the number of generations needed vs a single one.

- This mirrors real evolutionary biology : diversity in
  a population accelerates the emergence of optimal traits.
""")