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
from sklearn.svm import LinearSVC
# for get the probability 
from sklearn.calibration import CalibratedClassifierCV


# Model Evaluation
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


train_file_path = 'model_training/dataset/train.csv'
test_filename_path = 'model_training/dataset/test.csv'
train = pd.read_csv(train_file_path)
test = pd.read_csv(test_filename_path)


def evaluation(classifier):
    test_text = test['Statement']
    test_y = test['Label']
    predictions = classifier.predict(test_text)
    print('Confusion Matrix: \n',confusion_matrix(test_y,predictions))  
    print('Classification Report: \n',classification_report(test_y,predictions))  
    print('Accuracy: ', accuracy_score(test_y, predictions))  


def model_training():
    # Data Cleaning and Lemmatization
    documents = []
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(train['Statement'])):  
        # Remove all the special characters, eg(#, $, %, ...)
        document = re.sub(r'\W', ' ', str(train['Statement'][sen]))

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

	#logistic regression classifier
    svm_pipeline_ngram = Pipeline([
        ('svm_tfidf',tfidfconverter),
        ('svm_clf',CalibratedClassifierCV(base_estimator= LinearSVC(penalty='l2', dual=False), cv=5))
        ])

    svm_pipeline_ngram.fit(documents,train['Label'])

    evaluation(svm_pipeline_ngram)

	#saving best model to the disk
    pickle.dump(svm_pipeline_ngram,open('model.sav','wb'))

if __name__ == '__main__':
    model_training()