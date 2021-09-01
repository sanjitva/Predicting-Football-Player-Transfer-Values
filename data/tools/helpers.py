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


def clean_char(df):
    
    special_char = ['\xad','À','Á','Ç','É','Ñ','Ó','Ö','Ø','Ü','ß',
                     'à','á','â','ã','ä','å','æ','ç','è','é','ê','ë',
                     'í','î','ï','ð','ñ','ò','ó','ô','ö','ø','ú','ü',
                     'ý','ă','ą','Ć','ć','Č','č','Đ','đ','ę','ě','ğ',
                     'İ','ı','ľ','Ł','ł','ń','ň','ō','ř','Ş','ş','Š',
                     'š','ů','Ž','ž','Ș','ș','ț']

    replacement = ['','A','A','C','E','N','O','O','O','U','ss',
                    'a','a','a','a','a','a','ae','c','e','e','e',
                    'e','i','i','i','d','n','o','o','o','o','o',
                    'u','u','y','a','a','C','c','C','c','D','d',
                    'e','e','g','I','i','l','L','l','n','n','o',
                    'r','S','s','S','s','u','Z','z','S','s','t']



    #Replacing Special characters in the 'Player' Column of the fbref dataframe.

    clean_players = []
    for a in df['Player']:

        string = a

        player_string = []
        for z in string:
            if z in special_char:
                for e in list(range(len(special_char))):
                    if z == special_char[e]:
                        player_string.append(replacement[e])
                    else:
                        pass
            else:
                player_string.append(z)
        player_string = ''.join(player_string)
        clean_players.append(player_string)



    df['Player'] = clean_players 
    return df



def clean_std(dataframe):

    original = []
    duplicate = []

    for a in dataframe['Player']:
        if a not in original:
            original.append(a)
        else:
            duplicate.append(a)
    
    mid_season_transfers = pd.DataFrame(columns = dataframe.columns)

    for a in duplicate:
        player = dataframe[dataframe['Player']==a]
        mid_season_transfers = mid_season_transfers.append(dataframe[dataframe['Player']==a])
    
    
    first = mid_season_transfers.iloc[::2]
    second = mid_season_transfers.iloc[1::2]
    
    midseason = []

    for a in list(range(len(first))):

        double_club_combined = pd.Series([first.iloc[a]['Player'],
                           [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                           first.iloc[a]['MP']+second.iloc[a]['MP'],
                            first.iloc[a]['Starts']+second.iloc[a]['Starts'],
                            first.iloc[a]['Min']+second.iloc[a]['Min'],
                           (first.iloc[a]['Min']+second.iloc[a]['Min'])/90,
                           first.iloc[a]['Gls']+second.iloc[a]['Gls'],
                           first.iloc[a]['Ast']+second.iloc[a]['Ast'],
                           first.iloc[a]['Non-Penalty Goals']+second.iloc[a]['Non-Penalty Goals'],
                           first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored'],
                           first.iloc[a]['Penalties Attempted']+second.iloc[a]['Penalties Attempted'],
                           first.iloc[a]['Yellow Cards']+second.iloc[a]['Yellow Cards'],
                           first.iloc[a]['Red Cards']+second.iloc[a]['Red Cards'],
                           (first.iloc[a]['Gls']+second.iloc[a]['Gls'])/90,
                           (first.iloc[a]['Ast']+second.iloc[a]['Ast'])/90,
                           ((first.iloc[a]['Gls']+second.iloc[a]['Gls'])+(first.iloc[a]['Ast']+second.iloc[a]['Ast']))/90,
                           ((first.iloc[a]['Gls']+second.iloc[a]['Gls'])-(first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored']))/90,
                           ((first.iloc[a]['Gls']+second.iloc[a]['Gls'])+(first.iloc[a]['Ast']+second.iloc[a]['Ast'])-(first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored']))/90,
                           first.iloc[a]['xG']+second.iloc[a]['xG'],
                           first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'],
                           first.iloc[a]['xA']+second.iloc[a]['xA'],
                           first.iloc[a]['Non-penalty xG+ xA']+second.iloc[a]['Non-penalty xG+ xA'],
                           (first.iloc[a]['xG']+second.iloc[a]['xG'])/90,
                           (first.iloc[a]['xA']+second.iloc[a]['xA'])/90,
                           ((first.iloc[a]['xG']+second.iloc[a]['xG'])+(first.iloc[a]['xA']+second.iloc[a]['xA']))/90,
                           (first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'])/90,
                           (first.iloc[a]['Non-penalty xG+ xA']+second.iloc[a]['Non-penalty xG+ xA'])/90])

        midseason.append(double_club_combined)

    transferred_players = pd.DataFrame(midseason)
    transferred_players.columns = ['Player','Squad','MP','Starts','Min',
                                   'Total Mins/90','Gls','Ast','Non-Penalty Goals',
                                    'Penalties Scored','Penalties Attempted','Yellow Cards',
                                   'Red Cards','Gls/90','Ast/90','(G+A)/90','Non-Penalty Goals/90',
                                   '(Gls+Ast-Scored Penalties)/90','xG','Non-Penalty xG','xA',
                                    'Non-penalty xG+ xA','xG/90','xA/90','(xG+xA)/90',
                                     'Non-Penalty xG/90','(Non-Penalty xG+xA)/90']
    
    final_df = pd.concat([dataframe, mid_season_transfers, mid_season_transfers]).drop_duplicates(keep=False)
    final_df = pd.concat([final_df,transferred_players])
    return final_df
    

def check_dupes(dataframe):

    original = []
    duplicate = []

    for a in dataframe['Player']:
        if a not in original:
            original.append(a)
        else:
            duplicate.append(a)

    mid_season_transfers = pd.DataFrame(columns = dataframe.columns)

    for a in duplicate:
        player = dataframe[dataframe['Player']==a]
        mid_season_transfers = mid_season_transfers.append(dataframe[dataframe['Player']==a])
    
    return mid_season_transfers
