"""
Naive-bayes, Logistic Regression, Linear SVM, SVM Stochastic gradient decent and Random forest classifiers 
"""
import DataPreprocessrocess
import FeatureSelection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB    # using Naive Bayes's "MultinoialNB", classifier, to classify text


#building classifier using naive bayes 
nb_pipeline = Pipeline([('NBCV',FeatureSelection.countV),('nb_clf',MultinomialNB())])
nb_pipeline.fit(DataPreprocess.train_news['Statement'],DataPreprocess.train_news['Label'])

predicted_nb = nb_pipeline.predict(DataPreprocess.test_news['Statement'])
np.mean(predicted_nb == DataPreprocess.test_news['Label'])

#User defined functon for K-Fold cross validatoin
def build_confusion_matrix(classifier):
    
    k_fold = KFold(n=len(DataPreprocess.train_news), n_folds=5)
    scores = []
    confusion = np.array([[0,0],[0,0]])

    for train_ind, test_ind in k_fold:
        train_text = DataPreprocess.train_news.iloc[train_ind]['Statement'] 
        train_y = DataPreprocess.train_news.iloc[train_ind]['Label']
    
        test_text = DataPreprocess.train_news.iloc[test_ind]['Statement']
        test_y = DataPreprocess.train_news.iloc[test_ind]['Label']
        
        classifier.fit(train_text,train_y)
        predictions = classifier.predict(test_text)
        
        confusion += confusion_matrix(test_y,predictions)
        score = f1_score(test_y,predictions)
        scores.append(score)
    
    return (print('Total statements classified:', len(DataPreprocess.train_news)),
    print('Score:', sum(scores)/len(scores)),
    print('score length', len(scores)),
    print('Confusion matrix:'),
    print(confusion))


#K-fold cross validation for all classifiers
build_confusion_matrix(nb_pipeline)
