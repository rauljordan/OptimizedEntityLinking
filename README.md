Optimized Entity Linking Through Wikipedia
========

## Overview
We provide a simple interface for Named-Entity Linking and "wikification" of a passage of text using a variant of local search and the Wikipedia API as specified in our research paper 
[Search Optimizations in Named Entity Linking Systems](https://www.dropbox.com/s/suj1x2y82t2zt56/OptimizedEntityLinking.pdf?dl=0). 

Given a passage of text, such as "China has a large population", our system will link every keyword in that passage to its corresponding wikipedia page with a high confidence score through the modification of alpha, a parameter that can be specified at runtime.

## How to Run 
First install all pip requirements using `pip install -r requirements.txt`. Then, navigate to a python shell and run `import nltk` and run `nltk.download()`. This will download the Natural Language Toolkit, a crucial component of the project. Once `nltk.download()` is run, a window will come up where some necessary packages need to be downloaded. For this project, navigate to packages and download 

Now, navigate to the OptimizedEntityLinking folder and run

`python core.py "China has a large population" --alpha 0.9 --iterations 1` 

Where the first argument to core.py is the input text you wish to provide, alpha is an accuracy parameter that can be tweaked to improve the accuracy of the system as described in the paper from 0 to 1, and iterations is the number of iterations you wish to run local search for. We recommend just one iteration for reasons of speed. 

## Testing
To run our tests, simply run `python test.py`, which will return a list of accuracy scores from 0 to 1 of different values of alpha as specified in the file. This runs the algorithm over different test examples and solutions to discover the accuracy of the entity linking as alpha changes. This is also mentioned within the paper. 

### Issues

Please report any bugs or requests that you have using the GitHub issue tracker!

### Development

If you wish to contribute, first make your changes. Then submit a pull request
