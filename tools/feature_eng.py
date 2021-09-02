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


def rank_df(df):
    
    warnings.filterwarnings('ignore')
    
    def Diff(li1, li2):
        return list(set(li1) - set(li2)) + list(set(li2) - set(li1))
    
    
    all_columns = [a for a in df.columns]
    
    object_columns = ['Club','Position','Nation','Contract Years Left','League',
                      'Squad (20/21)','Squad (19/20)','Squad (18/19)','Squad (17/18)']
                      
                      
    
    all_rankable_columns = Diff(all_columns,object_columns)
    
    better_lower_columns = ['Yellow Cards (20/21)',
                'Red Cards (20/21)',
                'Total Failed Attempts at Controlling Ball (20/21)',
                'Number of Times Tackled when Dribbling (20/21)',
                'Number of Times Dribbled Past (20/21)',
                'Mistakes leading to Opponent Shots (20/21)',
                '2nd Yellow Cards (20/21)',
                'Fouls Committed (20/21)',
                'Offsides (20/21)',
                'Own Goals (20/21)',
                'Aerial Duel Lost (20/21)', 
                'Yellow Cards (19/20)',
                'Red Cards (19/20)',
                'Total Failed Attempts at Controlling Ball (19/20)',
                'Number of Times Tackled when Dribbling (19/20)',
                'Number of Times Dribbled Past (19/20)',
                'Mistakes leading to Opponent Shots (19/20)',
                '2nd Yellow Cards (19/20)',
                'Fouls Committed (19/20)',
                'Offsides (19/20)',
                'Own Goals (19/20)',
                'Aerial Duel Lost (19/20)',
                'Yellow Cards (18/19)',
                'Red Cards (18/19)',
                'Total Failed Attempts at Controlling Ball (18/19)',
                'Number of Times Tackled when Dribbling (18/19)',
                'Number of Times Dribbled Past (18/19)',
                'Mistakes leading to Opponent Shots (18/19)',
                '2nd Yellow Cards (18/19)',
                'Fouls Committed (18/19)',
                'Offsides (18/19)',
                'Own Goals (18/19)',
                'Aerial Duel Lost (18/19)',
                'Yellow Cards (17/18)',
                'Red Cards (17/18)',
                'Total Failed Attempts at Controlling Ball (17/18)',
                'Number of Times Tackled when Dribbling (17/18)',
                'Number of Times Dribbled Past (17/18)',
                'Mistakes leading to Opponent Shots (17/18)',
                '2nd Yellow Cards (17/18)',
                'Fouls Committed (17/18)',
                'Offsides (17/18)',
                'Own Goals (17/18)',
                'Aerial Duel Lost (17/18)']
  

    better_higher_columns = Diff(all_rankable_columns,better_lower_columns)
    
    for a in better_higher_columns:
        df[a] = df[a].rank(axis=0,method='min',na_option='keep',ascending=False)
    for a in better_lower_columns:
        df[a] = df[a].rank(axis=0,method='min',na_option='keep',ascending=True)
        
    return df  