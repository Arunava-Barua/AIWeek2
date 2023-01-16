import random
from typing import List, Tuple

def generate_k_sat(k: int, m: int, n: int) -> Tuple[List[List[int]], List[int]]:

    clauses = []
    variables = list(range(1, n+1))
    
    for i in range(m):
        clause = []
        for j in range(k):
            variable = random.choice(variables)
            negation = random.choice([-1, 1])
            clause.append(variable*negation)
        clauses.append(clause)
    return clauses, variables

k = 3
m = 10
n = 5
clauses, variables = generate_k_sat(k, m, n)
print(clauses)
print(variables)