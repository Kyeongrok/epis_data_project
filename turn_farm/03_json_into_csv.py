import pandas as pd


df = pd.read_json('turn_farm_with_family_info.json')
df.to_csv('turn_farm_with_family_info.csv')
print(df.head())