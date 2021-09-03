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

        cross_val_train = cross_val_score(lr, X_train_scaled, y_train, scoring="neg_root_mean_squared_error")
        cross_val_test = cross_val_score(lr, X_test_scaled, y_test, scoring="neg_root_mean_squared_error")
        
        scores_train.append(-(cross_val_train.mean()))
        scores_test.append(-(cross_val_test.mean()))
        
        
    print(f'Attackers Train RMSE = ${round(scores_train[0],2)}')
    print(f'Attackers Test RMSE = ${round(scores_test[0],2)}')
    print("----------------------------------------")
    print(f'Midfielders Train RMSE = ${round(scores_train[1],2)}')
    print(f'Midfielders Test RMSE = {round(scores_test[1],2)}')
    print("----------------------------------------")
    print(f'Defenders Train RMSE = ${round(scores_train[2],2)}')
    print(f'Defenders Test RMSE = ${round(scores_test[2],2)}')