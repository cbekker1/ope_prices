# this file requests the data and pulls into a dataframe

import requests
import pandas as pd
import os


store_name = "pnp"
url = f"https://openpricengine.com/api/v0.1/{store_name}"

response = requests.get(url)

if response.status_code == 200:
    data_df = pd.DataFrame(response.json(), index=[0])
    # Do something with the data
else:
    print(f"Error: {response.status_code} - {response.text}")
    

print(data_df.head())
print(data_df.columns)

# Next, save the DataFrame to a CSV file in the "data" directory
data_df.to_csv('../data/data_export.csv', index=False)
