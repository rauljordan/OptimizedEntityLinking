
from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(sublinear_tf=True, analyzer='word',
           stop_words='english')

documents = ["hello world this is awesome", "this is another page of wikipedia hello so awesome"]

response = vect.fit_transform(documents)

doc1 = response[0]
doc2 = response[1]

print doc1.getnnz()
print "Now Doc2"
print doc2.getnnz()

import numpy as np
