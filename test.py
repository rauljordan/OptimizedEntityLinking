
from __future__ import division
from OptimizedEntityLinking.core import EntityLinker
import json
import ast
import numpy as np

alphas = [0]

with open('test/solutions.txt') as f:
    solutions = []
    for line in f.readlines():
        solutions.append(ast.literal_eval(line))

with open('test/testset.txt') as f:
    avg_accuracies = []
    for alpha in alphas:
        el = EntityLinker(alpha, 1)
        accuracies = []
        for i, line in enumerate(f.readlines()):

            currentSolution = solutions[i]
            result = el.link(line)

            totalKeywords = len(result.keys())
            correctKeywords = 0
            for k in result:
                if result[k][0] == currentSolution[k][0]:
                    correctKeywords += 1

            accuracies.append(correctKeywords / totalKeywords)

        avg_accuracies.append(np.mean(accuracies))
        
print avg_accuracies
