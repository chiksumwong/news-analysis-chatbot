"""
Naive-bayes, Logistic Regression, Linear SVM, SVM Stochastic gradient decent and Random forest classifiers 
"""
import DataPreprocess
import FeatureSelection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB    # using Naive Bayes's "MultinoialNB", classifier, to classify text

from sklearn.cross_validation import KFold       # avoid 'Overfitting'

from sklearn.metrics import confusion_matrix, f1_score, classification_report

#logistic regression classifier
logR_pipeline_ngram = Pipeline([
        ('LogR_tfidf',FeatureSelection.tfidf_ngram),
        ('LogR_clf',LogisticRegression(penalty="l2",C=1))
        ])

logR_pipeline_ngram.fit(DataPreprocess.train_news['Statement'],DataPreprocess.train_news['Label'])
predicted_LogR_ngram = logR_pipeline_ngram.predict(DataPreprocess.test_news['Statement'])
np.mean(predicted_LogR_ngram == DataPreprocess.test_news['Label'])

#saving best model to the disk
model_file = 'final_model.sav'
pickle.dump(logR_pipeline_ngram,open(model_file,'wb'))
