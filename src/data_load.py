# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:23:08 2023

@author: cbek
"""
#%%

import os
home_repo = os.environ.get('MY_REPO_HOME')
os.chdir(home_repo+'\ope_prices\src')
from keywords import set_keywords
meat, staple_foods = set_keywords()
from data_extractor import extract_data

print('choose dates, a storetype and a set of keywords between meat and staple foods' )



#%% EXTRACT
product_keyword = meat

ope_df = extract_data(
    start_date='2023-01-01'
    ,end_date='2023-04-02'
    , product_keyword=product_keyword
    ,store_name='pnp'
    )

#%% rename df to contain keywords

def get_keyword_name(x=product_keyword):
    for name, value in globals().items():
        if value is x:
            return name
    return None  # variable not found

new_var_name = 'ope_df_' + get_keyword_name()
globals()[new_var_name] = ope_df
del ope_df, new_var_name

#%% LOAD
ope_df.to_csv('ope_prices/data/'+get_keyword_name()+'_prices_over_time.csv', index=False,mode='w')
