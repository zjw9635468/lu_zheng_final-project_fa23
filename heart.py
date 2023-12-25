import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
df = pd.read_csv('heart_disease.csv')

le = LabelEncoder()
df['Heart Disease']=le.fit_transform(df['Heart Disease'])

X = df.drop(columns=['Heart Disease'])
Y = df['Heart Disease']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)


xgb = XGBClassifier()
xgb.fit(X_train, Y_train)

def heart_result():
    testdata = pd.read_csv('heart_disease_input.csv')
    test_pred = xgb.predict(testdata)
    return test_pred