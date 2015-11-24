import wikipedia
# The Relevance Function 

# Given a link, a keyword, and a current state, how do we 
# figure out if that link is the best fit for that keyword 
# effectively using the context given to us? In our implementation, 
# there is a crucial consideration: we must be able to somehow 
# use previous assigned keywords as factors in our score. 
# This means that given the content of a wikipedia link, we must 
# use the current keyword and the keywords around it to gauge how 
# good of a match that link is to our current keyword. To 
# accomplish this task, we will discuss several implementations of
# different semantic-relatedness algorithms and approaches that 
# have been used in literature to take advantage of the structured 
# corpora of wikipedia. 

# A possible approach will be to use the Wikipedia Link-Based Measure
# weighed by a factor of relevance gamma obtained from the other
# keywords in the state. Much of this discussion will focus on
# determining gamma and the limitations of this approach.
def relevanceFunction(keyword, link):
	# get link "title" from url:
	link_title = link.split('/')[-1]

	# get associated page:
	p = wikipedia.page(link_title)

	# return the number of times the keyword appears in the content.
	return (len(p.content.split(keyword)) - 1)
	
    # if link == "Airplane":
    #     return 0.9
    # if link == "Dog":
    #     return 0.9
    # else:
    #     return 0.1
