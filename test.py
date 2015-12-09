
from OptimizedEntityLinking.core import EntityLinker
import json
import ast


alphas = [0, 0.25, 0.5, 0.99, 1]

with open('test/solutions.txt') as f:
    solutions = []
    for line in f.readlines():
        solutions.append(ast.literal_eval(line))

with open('test/testset.txt') as f:
    accuracies = []
    for alpha in alphas:
        el = EntityLinker(alpha, 1)
        for line in f.readlines():
            result = el.link(line)

            
