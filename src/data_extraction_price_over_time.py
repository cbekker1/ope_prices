
#%% 
# this file requests the data and pulls into a dataframe

import requests
import pandas as pd
import os

# set working directory to the folder that contains the cloned repository
# on your pc, create an environment variable named 'MY_REPO_HOME' with the folder path of where the git repo is cloned to

home_repo = os.environ.get('MY_REPO_HOME')
os.chdir(home_repo)
#%% 
# EXTRACT 

store_name = "pnp"

meat_keywords = ["Chicken", "Bacon", "Beef", "Pork", "Lamb"
                 , "Turkey", "Duck", "Goose", "Venison","Rabbit", "Quail"
                 , "Pheasant", "Ostrich"]

staple_foods = ["Rice", "Bread", "Pasta"
                , "Potatoes", "Beans", "Lentils", "Corn", "Oats"
                , "Wheat", "Barley", "Millet", "Cassava", "Yams", "Sweet potatoes"
                , "Plantains", "Quinoa", "Buckwheat", "Sorghum", "Rye"
                , "Chickpeas", "Peas", "Green peas"]

start_date = '2023-04-01'
end_date = '2023-04-02'

url = f"https://openpricengine.com/api/v0.1/{store_name}/products/query?"
params = {'productname':meat_keywords,
          'range':f'{start_date}to{end_date}',
          'currency':'Default',
          'store':'pnp'
          }
response = requests.get(url, params=params
                        )

if response.status_code == 200:
    data_df = pd.DataFrame([response.json()]).T
    # Do something with the data
else:
    print(f"Error: {response.status_code} - {response.text}")
    
#%% 
# TRANSFORM

data_df = data_df.rename(columns={data_df.columns[0]: 'products'})
data_df = pd.json_normalize(data_df['products'])
data_df = data_df.explode('Price over time')

# Get the keys of every dictionary in the "Price over time" column
keys = set()
for d in data_df['Price over time']:
    keys.update(d.keys())

# Add new columns to the DataFrame for every key in the set
for key in keys:
    data_df[key] = data_df['Price over time'].apply(lambda x: x.get(key))

#data_df = data_df.drop(['Price over time'], axis =1)

data_df = data_df.reindex(
    columns=['Date'
             , 'Price'
             , 'Product Name'
             , 'Country'
             ,'Continent'
             ,'Currency'
             ,'Store'
             ,'Category'
             ,'Product URL'
             ,'Price over time'
             ]).rename(
                 columns={'Product Name': 'ProductName'})




#%% LOAD
# data_df.to_csv('ope_prices/data/prices_over_time.csv', index=False,mode='w')