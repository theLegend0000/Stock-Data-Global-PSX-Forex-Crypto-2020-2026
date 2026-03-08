import pandas as pd
import os

folder = "15CoinsData"

all_data = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        
        coin = file.split("_")[0]   # get coin name
        
        df = pd.read_csv(f"{folder}/{file}")
        
        df["Coin"] = coin   # add coin column
        
        all_data.append(df)

# combine everything
combined_df = pd.concat(all_data, ignore_index=True)
print(df.head())

# save final dataset
combined_df.to_csv("combined_15coins_OHLCV.csv", index=False)