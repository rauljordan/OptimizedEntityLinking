


import wikipedia as wk

# cache = {"jobs": [("apple", "round fruit")], "cup": [("bra cup", "desc")] }

def getContentFromLink(link):
	try:
		linkText = wk.page(link, auto_suggest=False).content.lower()
	except wk.exceptions.DisambiguationError as e:
		options = filter(lambda x: "(disambiguation)" not in x, e.options)
		linkText = wk.page(options[0], auto_suggest=False).content.lower()
	return linkText

def getCache(wordArray):
	cache = {}
	for word in wordArray:
		links = wk.search(word)
		cache[word] = [(l, getContentFromLink(l)) for l in links]
	return cache


a = getCache(["apple"])

print len(a["apple"])