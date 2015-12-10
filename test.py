
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

            totalKeywords = len(result.keys())
            correctKeywords = 0
            for k in result:
                if result[k][0] == currentSolution[k]:
                    correctKeywords += 1

            accuracies.append(correctKeywords / totalKeywords)

        avg_accuracies.append(np.mean(accuracies))
        
print avg_accuracies



# import nltk 
# with open('sample.txt', 'r') as f:
#     sample = f.read()


# sentences = nltk.sent_tokenize(sample)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

# def extract_entity_names(t):
#     entity_names = []
#     if hasattr(t, 'label') and t.label:
#         if t.label() == 'NE':
#             entity_names.append(' '.join([child[0] for child in t]))
#         else:
#             for child in t:
#                 entity_names.extend(extract_entity_names(child))
#     return entity_names

# entity_names = []
# for tree in chunked_sentences:
#     # Print results per sentence
#     # print extract_entity_names(tree)
#     print chunked_sentences
#     entity_names.extend(extract_entity_names(tree))

# # Print all entity names
# # print entity_names

# # Print unique entity names
# print set(entity_names)
