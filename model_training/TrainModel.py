import re
import pandas as pd
import pickle

# Lemmatization
from nltk.stem import WordNetLemmatizer

# Stop-words
from nltk.corpus import stopwords

# Tf-idf vector
from sklearn.feature_extraction.text import TfidfVectorizer

# For Model Training
from sklearn.pipeline import Pipeline
# Classifier Algorithm
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import  LogisticRegression
from sklearn.svm import LinearSVC
# for get the probability 
from sklearn.calibration import CalibratedClassifierCV

# Model Evaluation
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def model_training():
    data_file_path = 'model_training/train.csv'
    data = pd.read_csv(data_file_path)

    # Data Cleaning and Lemmatization
    documents = []
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(data['Statement'])):  
        # Remove all the special characters, eg(#, $, %, ...)
        document = re.sub(r'\W', ' ', str(data['Statement'][sen]))

        # remove all single characters, eg( Sam's, it will get "Sam", "s",which has no meaning, remvoe it)
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)

	# Feature Selection
    tfidfconverter = TfidfVectorizer(stop_words=stopwords.words('english'),ngram_range=(1,4),use_idf=True,smooth_idf=True)

    X_train, X_test, y_train, y_test = train_test_split(documents, data['Label'], test_size=0.2)  

    # Naive-Bayes Classifier
    nb_pipeline_ngram = Pipeline([
            ('nb_tfidf',tfidfconverter),
            ('nb_clf',MultinomialNB())])

    # Train model
    nb_pipeline_ngram.fit(X_train,y_train)

    # Model Evaluation
    y_pred = nb_pipeline_ngram.predict(X_test)
    print('')
    print('Naive-Bayes Classifier')
    print('Confusion Matrix: \n',confusion_matrix(y_test,y_pred))  
    print('Classification Report: \n',classification_report(y_test,y_pred))  
    print('Accuracy: ', accuracy_score(y_test,y_pred))  
    print('')

	# logistic Regression Classifier
    logR_pipeline_ngram = Pipeline([
            ('LogR_tfidf',tfidfconverter),
            ('LogR_clf',LogisticRegression(solver='liblinear',penalty="l2",C=1))
            ])

    logR_pipeline_ngram.fit(X_train,y_train)

    # evaluation(logR_pipeline_ngram)
    y_pred = logR_pipeline_ngram.predict(X_test)
    print('logistic Regression Classifier')                                                              
    print('Confusion Matrix: \n',confusion_matrix(y_test,y_pred))  
    print('Classification Report: \n',classification_report(y_test,y_pred))  
    print('Accuracy: ', accuracy_score(y_test,y_pred))  
    print('')

    svm_pipeline_ngram = Pipeline([
        ('svm_tfidf',tfidfconverter),
        ('svm_clf',CalibratedClassifierCV(base_estimator= LinearSVC(penalty='l2', dual=False), cv=5))
        ])

    svm_pipeline_ngram.fit(X_train, y_train)
    # Model Evaluation
    y_pred = svm_pipeline_ngram.predict(X_test)     
    print('SVM Classifier')                                                              
    print('Confusion Matrix: \n',confusion_matrix(y_test,y_pred))  
    print('Classification Report: \n',classification_report(y_test,y_pred))  
    print('Accuracy: ', accuracy_score(y_test,y_pred))  
    print('')

	#saving best model to the disk
    pickle.dump(svm_pipeline_ngram,open('model_training/model.sav','wb'))

if __name__ == '__main__':
    model_training()