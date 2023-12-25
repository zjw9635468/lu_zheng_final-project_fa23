import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('kidney_disease.csv')
df = df.drop(columns=['id','sg','al','su','pc','pcc','ba','sod','pot','hemo','pcv','htn','dm','cad','pe'])
df['wc'] = pd.to_numeric(df['wc'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')
df['classification'] = df['classification'].replace(to_replace = {'ckd\t': 'ckd', 'notckd': 'not ckd'})
df['classification'] = df['classification'].map({'ckd': 0, 'not ckd': 1})
df['classification'] = pd.to_numeric(df['classification'], errors='coerce')
for col in df.columns:
    random_sample = df[col].dropna().sample(df[col].isna().sum())
    random_sample.index = df[df[col].isnull()].index
    df.loc[df[col].isnull(), col] = random_sample
for col in [col for col in df.columns if df[col].dtype == 'object']:
    print(f"{col} has {df[col].nunique()} categories\n")

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in [col for col in df.columns if df[col].dtype == 'object']:
    df[col] = le.fit_transform(df[col])

X = df.drop(columns=['classification'])  # Drop the 'target' column to get the features
Y = df['classification']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
classifier = RandomForestClassifier()
classifier.fit(X_train, Y_train)

def kindey_result():
    testdata = pd.read_csv('kidney_disease_input.csv')
    test_pred = classifier.predict(testdata)
    return test_pred