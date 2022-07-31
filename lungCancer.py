import joblib
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def predictLungCancer(userInp):
    userInput = np.array(userInp)
    userInput = userInput.reshape((1, -1))
    knn_from_joblib = joblib.load('lung_logreg.pkl')
    result = knn_from_joblib.predict(userInput)
    print("Ans from lungCancer : ", result)
    return result
