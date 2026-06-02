import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn import model_selection, preprocessing
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/raw/admission.csv')

X = df.drop(['Chance of Admit ','Unnamed: 0'], axis=1)
y = df['Chance of Admit ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=789)

lr = LinearRegression()
lr.fit(X_train, y_train)