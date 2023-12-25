import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('diabetes.csv')
df.replace({'Pregnancies':0,
            'Glucose':0,
            'BloodPressure':0,
            'SkinThickness':0,
            'Insulin':0,
            'BMI':0,
            'DiabetesPedigreeFunction':0,
            'Age':0},np.nan,inplace=True)
df['Pregnancies'] = df['Pregnancies'].fillna(df['Pregnancies'].mode()[0])
df['Glucose'] = df['Glucose'].fillna(df['Glucose'].mode()[0])
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].mode()[0])
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].mode()[0])
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].mode()[0])
df['BMI'] = df['BMI'].fillna(df['BMI'].mode()[0])

df['Pregnancies'] = df['Pregnancies'].astype('int')
df['Glucose'] = df['Glucose'].astype('int')
df['SkinThickness'] = df['SkinThickness'].astype('int')
df['Insulin'] = df['Insulin'].astype('int')
df['BloodPressure'] = df['BloodPressure'].astype('int')
Features_with_outliers = ['Pregnancies', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                          'DiabetesPedigreeFunction', 'Age']


def remove_outliers_iqr(data):
    # Calculate the first quartile (Q1) and third quartile (Q3)
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)

    # Calculate the interquartile range (IQR)
    IQR = Q3 - Q1

    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Remove outliers
    data = np.where(data > upper_bound, upper_bound, np.where(data < lower_bound, lower_bound, data))

    return data[(data >= lower_bound) & (data <= upper_bound)]

for column in Features_with_outliers:
    df[column] = remove_outliers_iqr(df[column])

X = df.drop(columns=['Outcome'])  # Drop the 'target' column to get the features
Y = df['Outcome']  # Scelect only the 'target' column as the target variable


X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 0.2, random_state = 5)


regressor = LogisticRegression()
regressor = regressor.fit(X_train, Y_train)
def diabetes_result():
    testdata = pd.read_csv('diabetes_input.csv')
    test_pred = regressor.predict(testdata)
    return test_pred

if __name__ == '__main__':
    print(diabetes_result())