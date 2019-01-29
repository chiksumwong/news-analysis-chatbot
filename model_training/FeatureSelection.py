"""
This file contains all the feature extraction and selection functions
For feature selection, we have used methods like simple bag-of-words and n-grams
word2vec and POS tagging to extract the features
Term frequency like tf-tdf weighting. 
"""
import DataPreprocess

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


"""
Start with bag of words
Step 1: tokenizing
Step 2: counting
Step 3: normalizing
"""

countV = CountVectorizer()
train_count = countV.fit_transform(DataPreprocess.train_news['Statement'].values)

print(countV)
print(train_count)

