"""
This file contains all the data preprocessing functions
"""
import pandas as pd   # handle csv file and data, as excel
import numpy as np    # math

import seaborn as sns # as Matplot API, data visualization
import matplotlib.pyplot as plt

import nltk           # Natural Language Tool Kit
from nltk.stem import SnowballStemmer

# read the dataset
train_filename = 'liar_dataset/train.csv'
test_filename = 'liar_dataset/test.csv'
valid_filename = 'liar_dataset/valid.csv'

train_news = pd.read_csv(train_filename)
test_news = pd.read_csv(test_filename)
valid_news = pd.read_csv(valid_filename)


"""
Exploratory data analysis
"""
# data overview
def data_ov():
    print("training dataset size:")
    print(train_news.shape)
    print(train_news.head(5))
    print("testing dataset size:")
    print(test_news.shape)
    print(test_news.head(5))
    print("validing dataset size:")
    print(valid_news.shape)
    print(valid_news.head(5))
# data_ov()


# Response variable distribution - The rate of true and false
def view_label_countplot(dataFile):
    sns.countplot(x='Label', data=dataFile)
    return plt.show()
# view_label_countplot(train_news)
# view_label_countplot(test_news)
# view_label_countplot(valid_news)


# Data quality checks - Check the data wether has null
def null_check():
    print("Checking data whether has null...")
    train_news.isnull().sum()
    train_news.info()
    test_news.isnull().sum()
    test_news.info()
    valid_news.isnull().sum()
    valid_news.info()
    print("check finished.")
# null_check()


"""
Preprocessing: tokenizing and stemming
"""
eng_stemmer = SnowballStemmer('english')
stopwords = set(nltk.corpus.stopwords.words('english'))

#Stemming
def stem_tokens(tokens, stemmer):
    stemmed = []
    for token in tokens:
        stemmed.append(stemmer.stem(token))
    return stemmed

#process the data
def process_data(data,exclude_stopword=True,stem=True):
    tokens = [w.lower() for w in data]
    tokens_stemmed = tokens
    tokens_stemmed = stem_tokens(tokens, eng_stemmer)
    tokens_stemmed = [w for w in tokens_stemmed if w not in stopwords ]
    return tokens_stemmed
