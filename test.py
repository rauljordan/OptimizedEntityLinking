
from __future__ import division
from OptimizedEntityLinking.core import EntityLinker
import json
import ast
import numpy as np

alphas = [0,0.25,0.5,0.75,1]

with open('test/solutions.txt') as f:
    solutions = []
    for line in f.readlines():
        solutions.append(ast.literal_eval(line))

# print solutions[0]['Thermodynamics']
# quit()

with open('test/testset.txt') as f:
    avg_accuracies = []
    for alpha in alphas:
        el = EntityLinker(alpha, 1)
        accuracies = []
        for i, line in enumerate(f.readlines()):

            currentSolution = solutions[i]
            result = el.link(line)
            print "result is:"
            print result
            print "solution is:"
            print currentSolution
            totalKeywords = len(result.keys())
            correctKeywords = 0
            for k in result:
                print result[k][0]
                print currentSolution[k][0]
                print result[k][0] == currentSolution[k][0]
                if result[k][0] == currentSolution[k][0]:
                    correctKeywords += 1
            print "correctKeywords: "
            print correctKeywords
            print "totalKeywords"
            print totalKeywords
            accuracies.append(correctKeywords / totalKeywords)
            print "accuracies:"
            print accuracies
        avg_accuracies.append(np.mean(accuracies))
        accuracies = []
        f.seek(0)
        
print avg_accuracies
