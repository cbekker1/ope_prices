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
meat, staple_foods, stores = set_keywords()
from data_extractor import extract_data, price_calc, calculate_metrics
from datetime import datetime

print('Choose dates, a storetype and a set of\
      keywords between meat and staple_foods')
print('Choose one of the available stores:'\
      + str(stores))


#%% EXTRACT
product_keyword = meat
store = 'pnp'
start_date, end_date = '2023-03-01', '2023-04-01'

ope_df = extract_data(
    start_date=start_date
    ,end_date=end_date
    , product_keyword=product_keyword
    ,store_name=store
    )


#%% TRANSFORM

ope_df = price_calc(ope_df)

#%% get keyword and change formats for naming purposes

def get_keyword_name(x=product_keyword):
    for name, value in globals().items():
        if value is x:
            return name
    return None  # variable not found

# Convert start_date to dd_mmm_yy format
start_date = datetime.strptime(start_date, '%Y-%m-%d').strftime('%d_%b_%y')

# Convert end_date to dd_mmm_yy format
end_date = datetime.strptime(end_date, '%Y-%m-%d').strftime('%d_%b_%y')

ope_df['ProductKeyword'] = get_keyword_name()

#%% CALCULATE METRICS

metrics_df = calculate_metrics(ope_df).rename(
    columns={'ProductName': 'UniqueProductCount'})
metrics_df['ProductKeyword'] = get_keyword_name()
metrics_df['StoreName'] = store

#%% LOAD

os.chdir(home_repo+'\ope_prices\data')
ope_df.to_csv(store+'_'+get_keyword_name(product_keyword)+ '_prices_from_'+start_date+'_till_'+end_date+'.csv'
              , index=False
              ,mode='w'
              )

metrics_df.to_csv('metrics_'+store+'_'+get_keyword_name(product_keyword)+ '_from_'+start_date+'_till_'+end_date+'.csv'
              , index=False
              ,mode='w'
              )

