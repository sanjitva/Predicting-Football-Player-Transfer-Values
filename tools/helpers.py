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
    final_df = final_df.reset_index(drop=True)
    return final_df
    


    
    
    
def clean_shooting(dataframe):
    
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
        if (first.iloc[a]['Total Shots'] + second.iloc[a]['Total Shots']) == 0 or (first.iloc[a]['Total Shots on Target'] + second.iloc[a]['Total Shots on Target']) == 0:

            double_club_combined = pd.Series([first.iloc[a]['Rk'],
                                          first.iloc[a]['Player'],
                                          first.iloc[a]['Nation'],
                                          first.iloc[a]['Pos'],
                                          [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                                          first.iloc[a]['Age'],
                                          first.iloc[a]['Born'],
                                          first.iloc[a]['90s▼']+second.iloc[a]['90s▼'],
                                          first.iloc[a]['Gls']+second.iloc[a]['Gls'],
                                          first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots'],
                                          first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target'],
                                          0,
                                          (first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots'])/90,
                                          (first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target'])/90,
                                          0,
                                          0,
                                          (first.iloc[a]['Avg Shot Distance (yds)']+second.iloc[a]['Avg Shot Distance (yds)'])/2,
                                          first.iloc[a]['Freekick Shots']+second.iloc[a]['Freekick Shots'],
                                          first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored'],
                                          first.iloc[a]['Penalties Attempted']+second.iloc[a]['Penalties Attempted'],
                                          first.iloc[a]['xG']+second.iloc[a]['xG'],
                                          first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'],
                                          0,
                                          (first.iloc[a]['Gls']+second.iloc[a]['Gls'])-(first.iloc[a]['xG']+second.iloc[a]['xG']),
                                          ((first.iloc[a]['Gls']+second.iloc[a]['Gls'])-(first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored']))-(first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'])])



        else:

            double_club_combined = pd.Series([first.iloc[a]['Rk'],
                                              first.iloc[a]['Player'],
                                              first.iloc[a]['Nation'],
                                              first.iloc[a]['Pos'],
                                              [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                                              first.iloc[a]['Age'],
                                              first.iloc[a]['Born'],
                                              first.iloc[a]['90s▼']+second.iloc[a]['90s▼'],
                                              first.iloc[a]['Gls']+second.iloc[a]['Gls'],
                                              first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots'],
                                              first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target'],
                                              ((first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target'])/(first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots']))*100,
                                              (first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots'])/90,
                                              (first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target'])/90,
                                              (first.iloc[a]['Gls']+first.iloc[a]['Gls'])/(first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots']),
                                              (first.iloc[a]['Gls']+first.iloc[a]['Gls'])/(first.iloc[a]['Total Shots on Target']+second.iloc[a]['Total Shots on Target']),
                                              (first.iloc[a]['Avg Shot Distance (yds)']+second.iloc[a]['Avg Shot Distance (yds)'])/2,
                                              first.iloc[a]['Freekick Shots']+second.iloc[a]['Freekick Shots'],
                                              first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored'],
                                              first.iloc[a]['Penalties Attempted']+second.iloc[a]['Penalties Attempted'],
                                              first.iloc[a]['xG']+second.iloc[a]['xG'],
                                              first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'],
                                              (first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'])/(first.iloc[a]['Total Shots']+second.iloc[a]['Total Shots']),
                                              (first.iloc[a]['Gls']+second.iloc[a]['Gls'])-(first.iloc[a]['xG']+second.iloc[a]['xG']),
                                              ((first.iloc[a]['Gls']+second.iloc[a]['Gls'])-(first.iloc[a]['Penalties Scored']+second.iloc[a]['Penalties Scored']))-(first.iloc[a]['Non-Penalty xG']+second.iloc[a]['Non-Penalty xG'])])

        midseason.append(double_club_combined)
    
    transferred_players = pd.DataFrame(midseason)
    transferred_players.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s▼','Gls',
                                    'Total Shots','Total Shots on Target','Shots on Target%','Shots/90',
                                    'Shots on Target/90','Goals/Shots','Goals/Shots on Target',
                                    'Avg Shot Distance (yds)','Freekick Shots','Penalties Scored',
                                    'Penalties Attempted','xG','Non-Penalty xG','Non-Penalty xG/Shots',
                                    'Goals Scored minus xG','Non-Penalty Goals Scored minus Non-Penalty xG']

    final_df = pd.concat([dataframe, mid_season_transfers, mid_season_transfers]).drop_duplicates(keep=False)
    final_df = pd.concat([final_df,transferred_players])
    final_df = final_df.reset_index(drop=True)
    
    return final_df   
    
    
    
def clean_shot_creation(dataframe):

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

        double_club_combined = pd.Series([first.iloc[a]['Rk'],
                                              first.iloc[a]['Player'],
                                              first.iloc[a]['Nation'],
                                              first.iloc[a]['Pos'],
                                              [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                                              first.iloc[a]['Age'],
                                              first.iloc[a]['Born'],
                                              first.iloc[a]['90s▼']+second.iloc[a]['90s▼'],
                                              first.iloc[a]['Shot-Creating Actions']+second.iloc[a]['Shot-Creating Actions'],
                                              (first.iloc[a]['Shot-Creating Actions']+second.iloc[a]['Shot-Creating Actions'])/90,
                                              first.iloc[a]['Passes Leading to Shot Attempt']+second.iloc[a]['Passes Leading to Shot Attempt'],
                                              first.iloc[a]['Set-Piece Leading to Shot Attempt']+second.iloc[a]['Set-Piece Leading to Shot Attempt'],
                                              first.iloc[a]['Dribbles Leading to Shot Attempt']+second.iloc[a]['Dribbles Leading to Shot Attempt'],
                                              first.iloc[a]['Shots Leading to Shot Attempt']+second.iloc[a]['Shots Leading to Shot Attempt'],
                                              first.iloc[a]['Fouls Drawn Leading to Shot Attempt']+second.iloc[a]['Fouls Drawn Leading to Shot Attempt'],
                                              first.iloc[a]['Defensive Actions Leading to Shot Attempt']+second.iloc[a]['Defensive Actions Leading to Shot Attempt'],
                                              first.iloc[a]['Goal Creating Actions']+second.iloc[a]['Goal Creating Actions'],
                                              (first.iloc[a]['Goal Creating Actions']+second.iloc[a]['Goal Creating Actions'])/90,
                                              first.iloc[a]['Passes Leading to Goals']+second.iloc[a]['Passes Leading to Goals'],
                                              first.iloc[a]['Set-Piece Leading to Goals']+second.iloc[a]['Set-Piece Leading to Goals'],
                                              first.iloc[a]['Dribbles Leading to Goals']+second.iloc[a]['Dribbles Leading to Goals'],
                                              first.iloc[a]['Shots Leading to Goals']+second.iloc[a]['Shots Leading to Goals'],
                                              first.iloc[a]['Fouls Drawn Leading to Goals']+second.iloc[a]['Fouls Drawn Leading to Goals'],
                                              first.iloc[a]['Defensive Actions Leading to Goals']+second.iloc[a]['Defensive Actions Leading to Goals']])


        midseason.append(double_club_combined)

    transferred_players = pd.DataFrame(midseason)

    transferred_players.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s▼',
                                   'Shot-Creating Actions','Shot-Creating Actions/90',
                                   'Passes Leading to Shot Attempt','Set-Piece Leading to Shot Attempt',
                                   'Dribbles Leading to Shot Attempt','Shots Leading to Shot Attempt',
                                   'Fouls Drawn Leading to Shot Attempt','Defensive Actions Leading to Shot Attempt',
                                   'Goal Creating Actions','Goal Creating Actions/90','Passes Leading to Goals',
                                   'Set-Piece Leading to Goals','Dribbles Leading to Goals','Shots Leading to Goals',
                                   'Fouls Drawn Leading to Goals','Defensive Actions Leading to Goals']

    final_df = pd.concat([dataframe, mid_season_transfers, mid_season_transfers]).drop_duplicates(keep=False)
    final_df = pd.concat([final_df,transferred_players])
    final_df = final_df.reset_index(drop=True)
    return final_df    

    
    
    
    
    
def clean_possession(dataframe):

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
        
        if (first.iloc[a]['Total Attempted Dribbles'] + second.iloc[a]['Total Attempted Dribbles']) == 0:
           
        
            double_club_combined = pd.Series([first.iloc[a]['Rk'],
                                                  first.iloc[a]['Player'],
                                                  first.iloc[a]['Nation'],
                                                  first.iloc[a]['Pos'],
                                                  [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                                                  first.iloc[a]['Age'],
                                                  first.iloc[a]['Born'],
                                                  first.iloc[a]['90s']+second.iloc[a]['90s'],
                                                  first.iloc[a]['Touches']+second.iloc[a]['Touches'],
                                                  first.iloc[a]['Touches in Defensive Penalty Box']+second.iloc[a]['Touches in Defensive Penalty Box'],
                                                  first.iloc[a]['Touches in Defensive 3rd']+second.iloc[a]['Touches in Defensive 3rd'],
                                                  first.iloc[a]['Touches in Midfield 3rd']+second.iloc[a]['Touches in Midfield 3rd'],
                                                  first.iloc[a]['Touches in Attacking 3rd']+second.iloc[a]['Touches in Attacking 3rd'],
                                                  first.iloc[a]['Touches in Attacking Penalty Box']+second.iloc[a]['Touches in Attacking Penalty Box'],
                                                  first.iloc[a]['Touches in Open-play']+second.iloc[a]['Touches in Open-play'],
                                                  first.iloc[a]['Total Successful Dribbles']+second.iloc[a]['Total Successful Dribbles'],
                                                  first.iloc[a]['Total Attempted Dribbles']+second.iloc[a]['Total Attempted Dribbles'],
                                                  0,
                                                  first.iloc[a]['Total no. of Players Dribbles Past']+second.iloc[a]['Total no. of Players Dribbles Past'],
                                                  first.iloc[a]['Total Nutmegs']+second.iloc[a]['Total Nutmegs'],
                                                  first.iloc[a]['Total Carries']+second.iloc[a]['Total Carries'],
                                                  first.iloc[a]['Total Distance Carried the Ball']+second.iloc[a]['Total Distance Carried the Ball'],
                                                  first.iloc[a]['Total Distance Carried the Ball in Forward Direction']+second.iloc[a]['Total Distance Carried the Ball in Forward Direction'],
                                                  first.iloc[a]['Total Carries in Forward Direction']+second.iloc[a]['Total Carries in Forward Direction'],
                                                  first.iloc[a]['Carries into Final Third']+second.iloc[a]['Carries into Final Third'],
                                                  first.iloc[a]['Carries into Attacking Penalty Box']+second.iloc[a]['Carries into Attacking Penalty Box'],
                                                  first.iloc[a]['Total Failed Attempts at Controlling Ball']+second.iloc[a]['Total Failed Attempts at Controlling Ball'],
                                                  first.iloc[a]['Number of Times Tackled when Dribbling']+second.iloc[a]['Number of Times Tackled when Dribbling'],
                                                  first.iloc[a]['Number of Times Player was Pass Target']+second.iloc[a]['Number of Times Player was Pass Target'],
                                                  first.iloc[a]['Number of Times Received Pass']+second.iloc[a]['Number of Times Received Pass'],
                                                  ((first.iloc[a]['Number of Times Received Pass']+second.iloc[a]['Number of Times Received Pass'])/(first.iloc[a]['Number of Times Player was Pass Target']+second.iloc[a]['Number of Times Player was Pass Target']))*100,
                                                  first.iloc[a]['Progressive Passes Received']+second.iloc[a]['Progressive Passes Received']])

        
        else:
            double_club_combined = pd.Series([first.iloc[a]['Rk'],
                                                  first.iloc[a]['Player'],
                                                  first.iloc[a]['Nation'],
                                                  first.iloc[a]['Pos'],
                                                  [first.iloc[a]['Squad'],second.iloc[a]['Squad']],
                                                  first.iloc[a]['Age'],
                                                  first.iloc[a]['Born'],
                                                  first.iloc[a]['90s']+second.iloc[a]['90s'],
                                                  first.iloc[a]['Touches']+second.iloc[a]['Touches'],
                                                  first.iloc[a]['Touches in Defensive Penalty Box']+second.iloc[a]['Touches in Defensive Penalty Box'],
                                                  first.iloc[a]['Touches in Defensive 3rd']+second.iloc[a]['Touches in Defensive 3rd'],
                                                  first.iloc[a]['Touches in Midfield 3rd']+second.iloc[a]['Touches in Midfield 3rd'],
                                                  first.iloc[a]['Touches in Attacking 3rd']+second.iloc[a]['Touches in Attacking 3rd'],
                                                  first.iloc[a]['Touches in Attacking Penalty Box']+second.iloc[a]['Touches in Attacking Penalty Box'],
                                                  first.iloc[a]['Touches in Open-play']+second.iloc[a]['Touches in Open-play'],
                                                  first.iloc[a]['Total Successful Dribbles']+second.iloc[a]['Total Successful Dribbles'],
                                                  first.iloc[a]['Total Attempted Dribbles']+second.iloc[a]['Total Attempted Dribbles'],
                                                  ((first.iloc[a]['Total Successful Dribbles']+second.iloc[a]['Total Successful Dribbles'])/(first.iloc[a]['Total Attempted Dribbles']+second.iloc[a]['Total Attempted Dribbles']))*100,
                                                  first.iloc[a]['Total no. of Players Dribbles Past']+second.iloc[a]['Total no. of Players Dribbles Past'],
                                                  first.iloc[a]['Total Nutmegs']+second.iloc[a]['Total Nutmegs'],
                                                  first.iloc[a]['Total Carries']+second.iloc[a]['Total Carries'],
                                                  first.iloc[a]['Total Distance Carried the Ball']+second.iloc[a]['Total Distance Carried the Ball'],
                                                  first.iloc[a]['Total Distance Carried the Ball in Forward Direction']+second.iloc[a]['Total Distance Carried the Ball in Forward Direction'],
                                                  first.iloc[a]['Total Carries in Forward Direction']+second.iloc[a]['Total Carries in Forward Direction'],
                                                  first.iloc[a]['Carries into Final Third']+second.iloc[a]['Carries into Final Third'],
                                                  first.iloc[a]['Carries into Attacking Penalty Box']+second.iloc[a]['Carries into Attacking Penalty Box'],
                                                  first.iloc[a]['Total Failed Attempts at Controlling Ball']+second.iloc[a]['Total Failed Attempts at Controlling Ball'],
                                                  first.iloc[a]['Number of Times Tackled when Dribbling']+second.iloc[a]['Number of Times Tackled when Dribbling'],
                                                  first.iloc[a]['Number of Times Player was Pass Target']+second.iloc[a]['Number of Times Player was Pass Target'],
                                                  first.iloc[a]['Number of Times Received Pass']+second.iloc[a]['Number of Times Received Pass'],
                                                  ((first.iloc[a]['Number of Times Received Pass']+second.iloc[a]['Number of Times Received Pass'])/(first.iloc[a]['Number of Times Player was Pass Target']+second.iloc[a]['Number of Times Player was Pass Target']))*100,
                                                  first.iloc[a]['Progressive Passes Received']+second.iloc[a]['Progressive Passes Received']])


        midseason.append(double_club_combined)

    transferred_players = pd.DataFrame(midseason)

    transferred_players.columns = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s','Touches',
                                   'Touches in Defensive Penalty Box','Touches in Defensive 3rd',
                                   'Touches in Midfield 3rd','Touches in Attacking 3rd',
                                   'Touches in Attacking Penalty Box','Touches in Open-play',
                                   'Total Successful Dribbles','Total Attempted Dribbles',
                                   'Dribble Success %','Total no. of Players Dribbles Past','Total Nutmegs',
                                   'Total Carries','Total Distance Carried the Ball',
                                   'Total Distance Carried the Ball in Forward Direction',
                                   'Total Carries in Forward Direction','Carries into Final Third',
                                   'Carries into Attacking Penalty Box','Total Failed Attempts at Controlling Ball',
                                   'Number of Times Tackled when Dribbling','Number of Times Player was Pass Target',
                                   'Number of Times Received Pass','% of Times Successfully Received Pass','Progressive Passes Received']

    final_df = pd.concat([dataframe, mid_season_transfers, mid_season_transfers]).drop_duplicates(keep=False)
    final_df = pd.concat([final_df,transferred_players])
    final_df = final_df.reset_index(drop=True)
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
