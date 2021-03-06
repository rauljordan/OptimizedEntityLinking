import nltk
def extract_entities(text):
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                print chunk.node, ' '.join(c[0] for c in chunk.leaves())


pos = nltk.pos_tag(nltk.word_tokenize(words))
keywords = [noun[0] for noun in pos if (noun[1] == 'NNP' or noun[1] == 'NN' or noun[1] == 'NNS')]
