"""
This module contains functions employed during the EDA process and for repeated processes during model testing. It is
used in the main Jupyter Notebook with the import statement 'import tools.helpers as th'.

CONTENTS:

Imports
I. Diagnostic Functions
II. Transformation Functions
"""

import numpy as np
import pandas as pd
import warnings
import itertools

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score



def baseline_linear_regression(df):

    attack = df[df['Position']=='attack']
    midfield = df[df['Position']=='midfield']
    defence = df[df['Position']=='Defender']

    positions =  [attack,midfield,defence]

    scores_train = []
    scores_test = []
    cross_val = []
    RMSE_val = []

    for position in positions:

        top_features = [a for a in position.corr()['Value'].sort_values(ascending=False)[:11].keys()]

        #Using top features identified earlier
        model_df = position[top_features]
        model_df = model_df.dropna()

        X = model_df.drop('Value',axis=1)
        y = model_df['Value']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,)

        ss= StandardScaler()
        lr = LinearRegression()

        X_train_scaled = ss.fit_transform(X_train)
        X_test_scaled = ss.transform(X_test)

        lr.fit(X_train_scaled,y_train);

        scores_train.append(lr.score(X_train_scaled,y_train))
        scores_test.append(lr.score(X_test_scaled,y_test))
        cross_val.append(cross_val_score(lr, X_test_scaled, y_test, cv=5, scoring="r2"))

        predictions = lr.predict(X_test_scaled)
        RMSE_val.append(round((mean_squared_error(y_test, predictions, squared=False)),2))

    print(f'Attackers Train Score = {scores_train[0]}')
    print(f'Attackers Test Score = {scores_test[0]}')
    print(f'Attackers Cross Validation Scores = {cross_val[0]}')
    print(f'RMSE = ${RMSE_val[0]}')
    print("----------------------------------------")
    print(f'Midfielders Train Score = {scores_train[1]}')
    print(f'Midfielders Test Score = {scores_test[1]}')
    print(f'Midfielders Cross Validation Scores = {cross_val[1]}')
    print(f'RMSE = ${RMSE_val[1]}')
    print("----------------------------------------")
    print(f'Defenders Train Score = {scores_train[2]}')
    print(f'Defenders Test Score = {scores_test[2]}')
    print(f'Defenders Cross Validation Scores = {cross_val[2]}')
    print(f'Defenders RMSE = ${RMSE_val[2]}')