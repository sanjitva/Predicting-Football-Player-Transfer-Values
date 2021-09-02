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
from functools import reduce
import tools.helpers as th


def fbref():

    #Importing English Premier League data from the 20/21 season. The column names were modified by me in MS Excel before importing them here.
    england_std21 = pd.read_excel('data/league_data/england/21/england_std.xlsx')
    england_shooting21 = pd.read_excel('data/league_data/england/21/england_shooting.xlsx')
    england_shot_creation21 = pd.read_excel('data/league_data/england/21/england_shot_creation.xlsx')
    england_possession21 = pd.read_excel('data/league_data/england/21/england_possession.xlsx')
    england_passing21 = pd.read_excel('data/league_data/england/21/england_passing.xlsx')
    england_defend21 = pd.read_excel('data/league_data/england/21/england_defending.xlsx')
    england_misc21 = pd.read_excel('data/league_data/england/21/england_misc.xlsx')



    # The column names were only edited for the files imported above. Therefore their column names will be used as a template to change the remaining columns
    std_cols = england_std21.columns
    shooting_cols = england_shooting21.columns
    shot_creation_cols = england_shot_creation21.columns
    possession_cols = england_possession21.columns
    passing_cols = england_passing21.columns
    defending_cols = england_defend21.columns
    misc_cols = england_misc21.columns


    #Importing English Premier League data from the 19/20 season.
    england_std20 = pd.read_excel('data/league_data/england/20/england_std.xlsx')
    england_std20.columns = std_cols

    england_shooting20 = pd.read_excel('data/league_data/england/20/england_shooting.xlsx')
    england_shooting20.columns = shooting_cols


    england_shot_creation20 = pd.read_excel('data/league_data/england/20/england_shot_creation.xlsx')
    england_shot_creation20.columns = shot_creation_cols


    england_possession20 = pd.read_excel('data/league_data/england/20/england_possession.xlsx')
    england_possession20.columns = possession_cols


    england_passing20 = pd.read_excel('data/league_data/england/20/england_passing.xlsx')
    england_passing20.columns = passing_cols


    england_defend20 = pd.read_excel('data/league_data/england/20/england_defending.xlsx')
    england_defend20.columns = defending_cols


    england_misc20 = pd.read_excel('data/league_data/england/20/england_misc.xlsx')
    england_misc20.columns = misc_cols





    #Importing English Premier League data from the 18/19 season.
    england_std19 = pd.read_excel('data/league_data/england/19/england_std.xlsx')
    england_std19.columns = std_cols

    england_shooting19 = pd.read_excel('data/league_data/england/19/england_shooting.xlsx')
    england_shooting19.columns = shooting_cols


    england_shot_creation19 = pd.read_excel('data/league_data/england/19/england_shot_creation.xlsx')
    england_shot_creation19.columns = shot_creation_cols


    england_possession19 = pd.read_excel('data/league_data/england/19/england_possession.xlsx')
    england_possession19.columns = possession_cols


    england_passing19 = pd.read_excel('data/league_data/england/19/england_passing.xlsx')
    england_passing19.columns = passing_cols


    england_defend19 = pd.read_excel('data/league_data/england/19/england_defending.xlsx')
    england_defend19.columns = defending_cols


    england_misc19 = pd.read_excel('data/league_data/england/19/england_misc.xlsx')
    england_misc19.columns = misc_cols




    #Importing English Premier League data from the 17/18 season.
    england_std18 = pd.read_excel('data/league_data/england/18/england_std.xlsx')
    england_std18.columns = std_cols

    england_shooting18 = pd.read_excel('data/league_data/england/18/england_shooting.xlsx')
    england_shooting18.columns = shooting_cols


    england_shot_creation18 = pd.read_excel('data/league_data/england/18/england_shot_creation.xlsx')
    england_shot_creation18.columns = shot_creation_cols


    england_possession18 = pd.read_excel('data/league_data/england/18/england_possession.xlsx')
    england_possession18.columns = possession_cols


    england_passing18 = pd.read_excel('data/league_data/england/18/england_passing.xlsx')
    england_passing18.columns = passing_cols


    england_defend18 = pd.read_excel('data/league_data/england/18/england_defending.xlsx')
    england_defend18.columns = defending_cols


    england_misc18 = pd.read_excel('data/league_data/england/18/england_misc.xlsx')
    england_misc18.columns = misc_cols




    #Importing French Ligue 1 data from the 20/21 season.
    france_std21 = pd.read_excel('data/league_data/france/21/france_std.xlsx')
    france_std21.columns = std_cols

    france_shooting21 = pd.read_excel('data/league_data/france/21/france_shooting.xlsx')
    france_shooting21.columns = shooting_cols


    france_shot_creation21 = pd.read_excel('data/league_data/france/21/france_shot_creation.xlsx')
    france_shot_creation21.columns = shot_creation_cols

    france_possession21 = pd.read_excel('data/league_data/france/21/france_possession.xlsx')
    france_possession21.columns = possession_cols


    france_passing21 = pd.read_excel('data/league_data/france/21/france_passing.xlsx')
    france_passing21.columns = passing_cols


    france_defend21 = pd.read_excel('data/league_data/france/21/france_defending.xlsx')
    france_defend21.columns = defending_cols


    france_misc21 = pd.read_excel('data/league_data/france/21/france_misc.xlsx')
    france_misc21.columns = misc_cols





    #Importing French Ligue 1 data from the 19/20 season.
    france_std20 = pd.read_excel('data/league_data/france/20/france_std.xlsx')
    france_std20.columns = std_cols

    france_shooting20 = pd.read_excel('data/league_data/france/20/france_shooting.xlsx')
    france_shooting20.columns = shooting_cols


    france_shot_creation20 = pd.read_excel('data/league_data/france/20/france_shot_creation.xlsx')
    france_shot_creation20.columns = shot_creation_cols


    france_possession20 = pd.read_excel('data/league_data/france/20/france_possession.xlsx')
    france_possession20.columns = possession_cols


    france_passing20 = pd.read_excel('data/league_data/france/20/france_passing.xlsx')
    france_passing20.columns = passing_cols


    france_defend20 = pd.read_excel('data/league_data/france/20/france_defending.xlsx')
    france_defend20.columns = defending_cols


    france_misc20 = pd.read_excel('data/league_data/france/20/france_misc.xlsx')
    france_misc20.columns = misc_cols



    #Importing French Ligue 1 data from the 18/19 season.
    france_std19 = pd.read_excel('data/league_data/france/19/france_std.xlsx')
    france_std19.columns = std_cols

    france_shooting19 = pd.read_excel('data/league_data/france/19/france_shooting.xlsx')
    france_shooting19.columns = shooting_cols


    france_shot_creation19 = pd.read_excel('data/league_data/france/19/france_shot_creation.xlsx')
    france_shot_creation19.columns = shot_creation_cols


    france_possession19 = pd.read_excel('data/league_data/france/19/france_possession.xlsx')
    france_possession19.columns = possession_cols


    france_passing19 = pd.read_excel('data/league_data/france/19/france_passing.xlsx')
    france_passing19.columns = passing_cols


    france_defend19 = pd.read_excel('data/league_data/france/19/france_defending.xlsx')
    france_defend19.columns = defending_cols


    france_misc19 = pd.read_excel('data/league_data/france/19/france_misc.xlsx')
    france_misc19.columns = misc_cols




    #Importing French Ligue 1 data from the 17/18 season.
    france_std18 = pd.read_excel('data/league_data/france/18/france_std.xlsx')
    france_std18.columns = std_cols

    france_shooting18 = pd.read_excel('data/league_data/france/18/france_shooting.xlsx')
    france_shooting18.columns = shooting_cols


    france_shot_creation18 = pd.read_excel('data/league_data/france/18/france_shot_creation.xlsx')
    france_shot_creation18.columns = shot_creation_cols


    france_possession18 = pd.read_excel('data/league_data/france/18/france_possession.xlsx')
    france_possession18.columns = possession_cols


    france_passing18 = pd.read_excel('data/league_data/france/18/france_passing.xlsx')
    france_passing18.columns = passing_cols


    france_defend18 = pd.read_excel('data/league_data/france/18/france_defending.xlsx')
    france_defend18.columns = defending_cols


    france_misc18 = pd.read_excel('data/league_data/france/18/france_misc.xlsx')
    france_misc18.columns = misc_cols



    #Importing German Bundesliga data from the 20/21 season.
    germany_std21 = pd.read_excel('data/league_data/germany/21/germany_std.xlsx')
    germany_std21.columns = std_cols

    germany_shooting21 = pd.read_excel('data/league_data/germany/21/germany_shooting.xlsx')
    germany_shooting21.columns = shooting_cols


    germany_shot_creation21 = pd.read_excel('data/league_data/germany/21/germany_shot_creation.xlsx')
    germany_shot_creation21.columns = shot_creation_cols

    germany_possession21 = pd.read_excel('data/league_data/germany/21/germany_possession.xlsx')
    germany_possession21.columns = possession_cols


    germany_passing21 = pd.read_excel('data/league_data/germany/21/germany_passing.xlsx')
    germany_passing21.columns = passing_cols


    germany_defend21 = pd.read_excel('data/league_data/germany/21/germany_defending.xlsx')
    germany_defend21.columns = defending_cols


    germany_misc21 = pd.read_excel('data/league_data/germany/21/germany_misc.xlsx')
    germany_misc21.columns = misc_cols







    #Importing German Bundesliga data from the 19/20 season.
    germany_std20 = pd.read_excel('data/league_data/germany/20/germany_std.xlsx')
    germany_std20.columns = std_cols

    germany_shooting20 = pd.read_excel('data/league_data/germany/20/germany_shooting.xlsx')
    germany_shooting20.columns = shooting_cols


    germany_shot_creation20 = pd.read_excel('data/league_data/germany/20/germany_shot_creation.xlsx')
    germany_shot_creation20.columns = shot_creation_cols


    germany_possession20 = pd.read_excel('data/league_data/germany/20/germany_possession.xlsx')
    germany_possession20.columns = possession_cols


    germany_passing20 = pd.read_excel('data/league_data/germany/20/germany_passing.xlsx')
    germany_passing20.columns = passing_cols


    germany_defend20 = pd.read_excel('data/league_data/germany/20/germany_defending.xlsx')
    germany_defend20.columns = defending_cols


    germany_misc20 = pd.read_excel('data/league_data/germany/20/germany_misc.xlsx')
    germany_misc20.columns = misc_cols





    #Importing German Bundesliga data from the 18/19 season.
    germany_std19 = pd.read_excel('data/league_data/germany/19/germany_std.xlsx')
    germany_std19.columns = std_cols

    germany_shooting19 = pd.read_excel('data/league_data/germany/19/germany_shooting.xlsx')
    germany_shooting19.columns = shooting_cols


    germany_shot_creation19 = pd.read_excel('data/league_data/germany/19/germany_shot_creation.xlsx')
    germany_shot_creation19.columns = shot_creation_cols


    germany_possession19 = pd.read_excel('data/league_data/germany/19/germany_possession.xlsx')
    germany_possession19.columns = possession_cols


    germany_passing19 = pd.read_excel('data/league_data/germany/19/germany_passing.xlsx')
    germany_passing19.columns = passing_cols


    germany_defend19 = pd.read_excel('data/league_data/germany/19/germany_defending.xlsx')
    germany_defend19.columns = defending_cols


    germany_misc19 = pd.read_excel('data/league_data/germany/19/germany_misc.xlsx')
    germany_misc19.columns = misc_cols



    #Importing German Bundesliga data from the 17/18 season.
    germany_std18 = pd.read_excel('data/league_data/germany/18/germany_std.xlsx')
    germany_std18.columns = std_cols

    germany_shooting18 = pd.read_excel('data/league_data/germany/18/germany_shooting.xlsx')
    germany_shooting18.columns = shooting_cols


    germany_shot_creation18 = pd.read_excel('data/league_data/germany/18/germany_shot_creation.xlsx')
    germany_shot_creation18.columns = shot_creation_cols


    germany_possession18 = pd.read_excel('data/league_data/germany/18/germany_possession.xlsx')
    germany_possession18.columns = possession_cols


    germany_passing18 = pd.read_excel('data/league_data/germany/18/germany_passing.xlsx')
    germany_passing18.columns = passing_cols


    germany_defend18 = pd.read_excel('data/league_data/germany/18/germany_defending.xlsx')
    germany_defend18.columns = defending_cols


    germany_misc18 = pd.read_excel('data/league_data/germany/18/germany_misc.xlsx')
    germany_misc18.columns = misc_cols



    #Importing Italian Serie A data from the 20/21 season.
    italy_std21 = pd.read_excel('data/league_data/italy/21/italy_std.xlsx')
    italy_std21.columns = std_cols

    italy_shooting21 = pd.read_excel('data/league_data/italy/21/italy_shooting.xlsx')
    italy_shooting21.columns = shooting_cols


    italy_shot_creation21 = pd.read_excel('data/league_data/italy/21/italy_shot_creation.xlsx')
    italy_shot_creation21.columns = shot_creation_cols

    italy_possession21 = pd.read_excel('data/league_data/italy/21/italy_possession.xlsx')
    italy_possession21.columns = possession_cols


    italy_passing21 = pd.read_excel('data/league_data/italy/21/italy_passing.xlsx')
    italy_passing21.columns = passing_cols


    italy_defend21 = pd.read_excel('data/league_data/italy/21/italy_defending.xlsx')
    italy_defend21.columns = defending_cols


    italy_misc21 = pd.read_excel('data/league_data/italy/21/italy_misc.xlsx')
    italy_misc21.columns = misc_cols


    #Importing Italian Serie A data from the 19/20 season.
    italy_std20 = pd.read_excel('data/league_data/italy/20/italy_std.xlsx')
    italy_std20.columns = std_cols

    italy_shooting20 = pd.read_excel('data/league_data/italy/20/italy_shooting.xlsx')
    italy_shooting20.columns = shooting_cols


    italy_shot_creation20 = pd.read_excel('data/league_data/italy/20/italy_shot_creation.xlsx')
    italy_shot_creation20.columns = shot_creation_cols


    italy_possession20 = pd.read_excel('data/league_data/italy/20/italy_possession.xlsx')
    italy_possession20.columns = possession_cols


    italy_passing20 = pd.read_excel('data/league_data/italy/20/italy_passing.xlsx')
    italy_passing20.columns = passing_cols


    italy_defend20 = pd.read_excel('data/league_data/italy/20/italy_defending.xlsx')
    italy_defend20.columns = defending_cols


    italy_misc20 = pd.read_excel('data/league_data/italy/20/italy_misc.xlsx')
    italy_misc20.columns = misc_cols


    #Importing Italian Serie A data from the 18/19 season.
    italy_std19 = pd.read_excel('data/league_data/italy/19/italy_std.xlsx')
    italy_std19.columns = std_cols

    italy_shooting19 = pd.read_excel('data/league_data/italy/19/italy_shooting.xlsx')
    italy_shooting19.columns = shooting_cols


    italy_shot_creation19 = pd.read_excel('data/league_data/italy/19/italy_shot_creation.xlsx')
    italy_shot_creation19.columns = shot_creation_cols


    italy_possession19 = pd.read_excel('data/league_data/italy/19/italy_possession.xlsx')
    italy_possession19.columns = possession_cols


    italy_passing19 = pd.read_excel('data/league_data/italy/19/italy_passing.xlsx')
    italy_passing19.columns = passing_cols


    italy_defend19 = pd.read_excel('data/league_data/italy/19/italy_defending.xlsx')
    italy_defend19.columns = defending_cols


    italy_misc19 = pd.read_excel('data/league_data/italy/19/italy_misc.xlsx')
    italy_misc19.columns = misc_cols


    #Importing Italian Serie A data from the 17/18 season.
    italy_std18 = pd.read_excel('data/league_data/italy/18/italy_std.xlsx')
    italy_std18.columns = std_cols

    italy_shooting18 = pd.read_excel('data/league_data/italy/18/italy_shooting.xlsx')
    italy_shooting18.columns = shooting_cols


    italy_shot_creation18 = pd.read_excel('data/league_data/italy/18/italy_shot_creation.xlsx')
    italy_shot_creation18.columns = shot_creation_cols


    italy_possession18 = pd.read_excel('data/league_data/italy/18/italy_possession.xlsx')
    italy_possession18.columns = possession_cols


    italy_passing18 = pd.read_excel('data/league_data/italy/18/italy_passing.xlsx')
    italy_passing18.columns = passing_cols


    italy_defend18 = pd.read_excel('data/league_data/italy/18/italy_defending.xlsx')
    italy_defend18.columns = defending_cols


    italy_misc18 = pd.read_excel('data/league_data/italy/18/italy_misc.xlsx')
    italy_misc18.columns = misc_cols



    #Importing Spanish La Liga data from the 20/21 season.
    spain_std21 = pd.read_excel('data/league_data/spain/21/spain_std.xlsx')
    spain_std21.columns = std_cols

    spain_shooting21 = pd.read_excel('data/league_data/spain/21/spain_shooting.xlsx')
    spain_shooting21.columns = shooting_cols


    spain_shot_creation21 = pd.read_excel('data/league_data/spain/21/spain_shot_creation.xlsx')
    spain_shot_creation21.columns = shot_creation_cols


    spain_possession21 = pd.read_excel('data/league_data/spain/21/spain_possession.xlsx')
    spain_possession21.columns = possession_cols


    spain_passing21 = pd.read_excel('data/league_data/spain/21/spain_passing.xlsx')
    spain_passing21.columns = passing_cols


    spain_defend21 = pd.read_excel('data/league_data/spain/21/spain_defending.xlsx')
    spain_defend21.columns = defending_cols


    spain_misc21 = pd.read_excel('data/league_data/spain/21/spain_misc.xlsx')
    spain_misc21.columns = misc_cols



    #Importing Spanish La Liga data from the 19/20 season.
    spain_std20 = pd.read_excel('data/league_data/spain/20/spain_std.xlsx')
    spain_std20.columns = std_cols

    spain_shooting20 = pd.read_excel('data/league_data/spain/20/spain_shooting.xlsx')
    spain_shooting20.columns = shooting_cols


    spain_shot_creation20 = pd.read_excel('data/league_data/spain/20/spain_shot_creation.xlsx')
    spain_shot_creation20.columns = shot_creation_cols


    spain_possession20 = pd.read_excel('data/league_data/spain/20/spain_possession.xlsx')
    spain_possession20.columns = possession_cols


    spain_passing20 = pd.read_excel('data/league_data/spain/20/spain_passing.xlsx')
    spain_passing20.columns = passing_cols


    spain_defend20 = pd.read_excel('data/league_data/spain/20/spain_defending.xlsx')
    spain_defend20.columns = defending_cols


    spain_misc20 = pd.read_excel('data/league_data/spain/20/spain_misc.xlsx')
    spain_misc20.columns = misc_cols



    #Importing Spanish La Liga data from the 18/19 season.
    spain_std19 = pd.read_excel('data/league_data/spain/19/spain_std.xlsx')
    spain_std19.columns = std_cols

    spain_shooting19 = pd.read_excel('data/league_data/spain/19/spain_shooting.xlsx')
    spain_shooting19.columns = shooting_cols


    spain_shot_creation19 = pd.read_excel('data/league_data/spain/19/spain_shot_creation.xlsx')
    spain_shot_creation19.columns = shot_creation_cols


    spain_possession19 = pd.read_excel('data/league_data/spain/19/spain_possession.xlsx')
    spain_possession19.columns = possession_cols

    spain_passing19 = pd.read_excel('data/league_data/spain/19/spain_passing.xlsx')
    spain_passing19.columns = passing_cols


    spain_defend19 = pd.read_excel('data/league_data/spain/19/spain_defending.xlsx')
    spain_defend19.columns = defending_cols


    spain_misc19 = pd.read_excel('data/league_data/spain/19/spain_misc.xlsx')
    spain_misc19.columns = misc_cols



    #Importing Spanish La Liga data from the 17/18 season.
    spain_std18 = pd.read_excel('data/league_data/spain/18/spain_std.xlsx')
    spain_std18.columns = std_cols

    spain_shooting18 = pd.read_excel('data/league_data/spain/18/spain_shooting.xlsx')
    spain_shooting18.columns = shooting_cols


    spain_shot_creation18 = pd.read_excel('data/league_data/spain/18/spain_shot_creation.xlsx')
    spain_shot_creation18.columns = shot_creation_cols


    spain_possession18 = pd.read_excel('data/league_data/spain/18/spain_possession.xlsx')
    spain_possession18.columns = possession_cols


    spain_passing18 = pd.read_excel('data/league_data/spain/18/spain_passing.xlsx')
    spain_passing18.columns = passing_cols


    spain_defend18 = pd.read_excel('data/league_data/spain/18/spain_defending.xlsx')
    spain_defend18.columns = defending_cols


    spain_misc18 = pd.read_excel('data/league_data/spain/18/spain_misc.xlsx')
    spain_misc18.columns = misc_cols




    # Grouping data by category for each season
    s21_std = pd.concat([england_std21,france_std21,germany_std21,italy_std21,spain_std21])
    s20_std = pd.concat([england_std20,france_std20,germany_std20,italy_std20,spain_std20])
    s19_std = pd.concat([england_std19,france_std19,germany_std19,italy_std19,spain_std19])
    s18_std = pd.concat([england_std18,france_std18,germany_std18,italy_std18,spain_std18])


    s21_shooting = pd.concat([england_shooting21,france_shooting21,germany_shooting21,italy_shooting21,spain_shooting21])
    s20_shooting = pd.concat([england_shooting20,france_shooting20,germany_shooting20,italy_shooting20,spain_shooting20])
    s19_shooting = pd.concat([england_shooting19,france_shooting19,germany_shooting19,italy_shooting19,spain_shooting19])
    s18_shooting = pd.concat([england_shooting18,france_shooting18,germany_shooting18,italy_shooting18,spain_shooting18])


    s21_shot_creation = pd.concat([england_shot_creation21,france_shot_creation21,germany_shot_creation21,italy_shot_creation21,spain_shot_creation21])
    s20_shot_creation = pd.concat([england_shot_creation20,france_shot_creation20,germany_shot_creation20,italy_shot_creation20,spain_shot_creation20])
    s19_shot_creation = pd.concat([england_shot_creation19,france_shot_creation19,germany_shot_creation19,italy_shot_creation19,spain_shot_creation19])
    s18_shot_creation = pd.concat([england_shot_creation18,france_shot_creation18,germany_shot_creation18,italy_shot_creation18,spain_shot_creation18])


    s21_possession = pd.concat([england_possession21,france_possession21,germany_possession21,italy_possession21,spain_possession21])
    s20_possession = pd.concat([england_possession20,france_possession20,germany_possession20,italy_possession20,spain_possession20])
    s19_possession = pd.concat([england_possession19,france_possession19,germany_possession19,italy_possession19,spain_possession19])
    s18_possession = pd.concat([england_possession18,france_possession18,germany_possession18,italy_possession18,spain_possession18])


    s21_passing = pd.concat([england_passing21,france_passing21,germany_passing21,italy_passing21,spain_passing21])
    s20_passing = pd.concat([england_passing20,france_passing20,germany_passing20,italy_passing20,spain_passing20])
    s19_passing = pd.concat([england_passing19,france_passing19,germany_passing19,italy_passing19,spain_passing19])
    s18_passing = pd.concat([england_passing18,france_passing18,germany_passing18,italy_passing18,spain_passing18])


    s21_defending = pd.concat([england_defend21,france_defend21,germany_defend21,italy_defend21,spain_defend21])
    s20_defending = pd.concat([england_defend20,france_defend20,germany_defend20,italy_defend20,spain_defend20])
    s19_defending = pd.concat([england_defend19,france_defend19,germany_defend19,italy_defend19,spain_defend19])
    s18_defending = pd.concat([england_defend18,france_defend18,germany_defend18,italy_defend18,spain_defend18])


    s21_misc = pd.concat([england_misc21,france_misc21,germany_misc21,italy_misc21,spain_misc21])
    s20_misc = pd.concat([england_misc20,france_misc20,germany_misc20,italy_misc20,spain_misc20])
    s19_misc = pd.concat([england_misc19,france_misc19,germany_misc19,italy_misc19,spain_misc19])
    s18_misc = pd.concat([england_misc18,france_misc18,germany_misc18,italy_misc18,spain_misc18])


    #Combining all data for ALL leagues season by season

    #20/21 Season
    s21 = [th.clean_std(th.clean_char(s21_std)),
           th.clean_shooting(th.clean_char(s21_shooting)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Gls','Penalties Scored','Penalties Attempted','xG','Non-Penalty xG'],axis=1),
           th.clean_shot_creation(th.clean_char(s21_shot_creation)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_possession(th.clean_char(s21_possession)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_passing(th.clean_char(s21_passing)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Passes that lead to a Shot'],axis=1),
           th.clean_defending(th.clean_char(s21_defending)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_misc(th.clean_char(s21_misc)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Yellow Cards', 'Red Cards','Tackles Won'],axis=1)]

    df21 = reduce(lambda left,right: pd.merge(left,right,on='Player'), s21)
    df21.columns = [a+' (20/21)' for a in df21.columns]
    df21.rename(columns={"Player (20/21)": "Player"},inplace=True)


    #19/20 Season
    s20 = [th.clean_std(th.clean_char(s20_std)),
           th.clean_shooting(th.clean_char(s20_shooting)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Gls','Penalties Scored','Penalties Attempted','xG','Non-Penalty xG'],axis=1),
           th.clean_shot_creation(th.clean_char(s20_shot_creation)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_possession(th.clean_char(s20_possession)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_passing(th.clean_char(s20_passing)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Passes that lead to a Shot'],axis=1),
           th.clean_defending(th.clean_char(s20_defending)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_misc(th.clean_char(s20_misc)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Yellow Cards', 'Red Cards','Tackles Won'],axis=1)]

    df20 = reduce(lambda left,right: pd.merge(left,right,on='Player'), s20)
    df20.columns = [a+' (19/20)' for a in df20.columns]
    df20.rename(columns={"Player (19/20)": "Player"},inplace=True)


    #18/19 Season
    s19 = [th.clean_std(th.clean_char(s19_std)),
           th.clean_shooting(th.clean_char(s19_shooting)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Gls','Penalties Scored','Penalties Attempted','xG','Non-Penalty xG'],axis=1),
           th.clean_shot_creation(th.clean_char(s19_shot_creation)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_possession(th.clean_char(s19_possession)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_passing(th.clean_char(s19_passing)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Passes that lead to a Shot'],axis=1),
           th.clean_defending(th.clean_char(s19_defending)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_misc(th.clean_char(s19_misc)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Yellow Cards', 'Red Cards','Tackles Won'],axis=1)]

    df19 = reduce(lambda left,right: pd.merge(left,right,on='Player'), s19)
    df19.columns = [a+' (18/19)' for a in df19.columns]
    df19.rename(columns={"Player (18/19)": "Player"},inplace=True)


    #17/18 Season
    s18 = [th.clean_std(th.clean_char(s18_std)),
           th.clean_shooting(th.clean_char(s18_shooting)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Gls','Penalties Scored','Penalties Attempted','xG','Non-Penalty xG'],axis=1),
           th.clean_shot_creation(th.clean_char(s18_shot_creation)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_possession(th.clean_char(s18_possession)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_passing(th.clean_char(s18_passing)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Passes that lead to a Shot'],axis=1),
           th.clean_defending(th.clean_char(s18_defending)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s'],axis=1),
           th.clean_misc(th.clean_char(s18_misc)).drop(['Rk','Nation', 'Pos', 'Squad', 'Age', 'Born', '90s','Yellow Cards', 'Red Cards','Tackles Won'],axis=1)]

    df18 = reduce(lambda left,right: pd.merge(left,right,on='Player'), s18)
    df18.columns = [a+' (17/18)' for a in df18.columns]
    df18.rename(columns={"Player (17/18)": "Player"},inplace=True)



    #Combining all data into one large final dataframe

    #Dataset containing information about the 20/21 and 19/20 seasons.
    two_season = pd.merge(df21, df20, how='outer')

    #Dataset containing information about the 20/21, 19/20 and 18/19 seasons.
    three_season = pd.merge(two_season, df19, how='outer')

    #Dataset containing information about the 20/21, 19/20, 18/19 and 17/18 seasons.
    four_season = pd.merge(three_season,df18, how='outer')

    return four_season


