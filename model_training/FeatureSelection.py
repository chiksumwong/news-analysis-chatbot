"""
This file contains all the feature extraction and selection functions
For feature selection, we have used methods like simple bag-of-words and n-grams
word2vec and POS tagging to extract the features
Term frequency like tf-tdf weighting. 
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

