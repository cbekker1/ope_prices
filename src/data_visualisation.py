# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:28:28 2023

@author: cbek
"""
#%%

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


#%% Set up Seaborn plotting defaults for data visualization best practices
sns.set_style("darkgrid")
sns.set_palette("colorblind")

#%% Create an empty dataframe to store the combined data
metrics_data_combined = pd.DataFrame()


#%% Loop over all CSV files in the "data" folder starting with "metrics_"
home_repo = os.environ.get('MY_REPO_HOME')
os.chdir(home_repo+'\ope_prices')
for file_name in os.listdir("data"):
    if file_name.startswith("metrics_") and file_name.endswith(".csv"):
        file_path = os.path.join("data", file_name)
        # Read the CSV file and append its data to the combined dataframe
        df = pd.read_csv(file_path)
        metrics_data_combined = metrics_data_combined.append(df)

#%% Convert the "Date" column to a datetime object for easier plotting
metrics_data_combined["Date"] = pd.to_datetime(metrics_data_combined["Date"])
metrics_data_combined['Month_Year'] = pd.to_datetime(metrics_data_combined['Date']).dt.strftime('%b %Y')

#%% Create a line plot with Seaborn
metrics_data_combined = metrics_data_combined.reset_index(drop=True)
plot_stores = sns.lineplot(
    data=metrics_data_combined,
    x="Date",
    y="PricesCumDiff",
    hue="StoreName",
    linewidth=2,
    markers=True,
    dashes=False
)

#%% Set the title and axis labels
# Get the unique values of the "ProductKeyword" column
product_keywords = metrics_data_combined["ProductKeyword"].unique()
# Combine the two strings to create the title of the plot
title = "Price changes over time by Retailer for " + ", ".join(product_keywords)

plot_stores.set_title(title)
plot_stores.set(xlabel="Month / Year")
# Rotate the x-axis labels by 45 degrees to improve readability
plot_stores.set_xticklabels(plot_stores.get_xticklabels(), rotation=45)
plot_stores.set_ylabel("PricesCumDiff")
# Format the y-axis as percentages
plot_stores.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

#%% Show the plot and save a png file with a picture
plt.show()
filename = "price_changes_over_time.png"
folder = "plots/"
i = 2
while os.path.exists(folder + filename):
    filename = "price_changes_over_time_" + str(i) + ".png"
    i += 1
plot_stores.figure.savefig(folder + filename, dpi=300)