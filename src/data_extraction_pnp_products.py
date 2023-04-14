# this file requests the data and pulls into a dataframe

import requests
import pandas as pd
import os


#store_name = "pnp"
url = "https://openpricengine.com/api/v0.1/pnp/products"
params = {'productname':'milk'
          ,'range':'2023-04-08to2023-04-10'
          ,'currency':'ZAR'
          }


response = requests.get(url, params=params)
data = response.json()
#data_df = pd.DataFrame([response.json()]).T.rename(columns={'0': 'column_name'})
data_df = pd.DataFrame([response.json()]).T
data_df = data_df.rename(columns={data_df.columns[0]: 'products'})


print(data_df.head())

data_df.to_csv('../data/data_export_params.csv', index=False,mode='w')
