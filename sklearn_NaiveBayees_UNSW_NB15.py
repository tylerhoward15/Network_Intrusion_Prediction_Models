from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

def run_naiveBayes(training_dataset, testing_dataset):
    training_nparray = training_dataset.to_numpy()  # This is necessary to correctly shape the array
    testing_nparray = testing_dataset.to_numpy()

    # Preprocess
    enc = preprocessing.OrdinalEncoder()

    encoded_dataset = enc.fit_transform(training_nparray)  # All categorical features are now numerical
    X_train = encoded_dataset[:, :-1]  # All rows, omit last column
    y_train = np.ravel(encoded_dataset[:, -1:])  # All rows, only the last column

    # Repeat preprocessing for test data
    encoded_dataset = enc.fit_transform(testing_nparray)
    X_test = encoded_dataset[:, :-1]
    y_test = np.ravel(encoded_dataset[:, -1:])

    # Fit to model and predict
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)

    total_datapoints = X_test.shape[0]
    mislabeled_datapoints = (y_test != y_pred).sum()
    correct_datapoints = total_datapoints - mislabeled_datapoints
    percent_correct = (correct_datapoints / total_datapoints) * 100

    print("NaiveBayes results for UNSW_NB15:\n")
    print("Total datapoints: %d\nCorrect datapoints: %d\nMislabeled datapoints: %d\nPercent correct: %.2f%%"
          % (total_datapoints, correct_datapoints, mislabeled_datapoints, percent_correct))




