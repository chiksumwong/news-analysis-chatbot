import pandas as pd
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def model_evaluate(model_path, description):
    test_data_path = 'model_training/test.csv'
    test_data = pd.read_csv(test_data_path)
    test_X = test_data['Statement']
    test_y = test_data['Label']

    model = pickle.load(open(model_path, 'rb'))
    predictions = model.predict(test_X)

    print(description)                                                              
    print('Confusion Matrix: \n',confusion_matrix(test_y, predictions))  
    print('Classification Report: \n',classification_report(test_y, predictions))  
    print('Accuracy: ', accuracy_score(test_y, predictions))  
    print('')


if __name__ == '__main__':
    nb_model_path = 'model_training/classifier_model/nb_model.sav'
    logR_model_path = 'model_training/classifier_model/logR_model.sav'
    svm_model_path = 'model_training/classifier_model/svm_model.sav'

    model_evaluate(nb_model_path, "Naive-Bayes Classifier")
    model_evaluate(logR_model_path, "Logistic Regression Classifier")
    model_evaluate(svm_model_path, "Line SVM Classifier")