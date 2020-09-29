import pandas as pd


# df = pd.read_json('turn_farm_with_family_info.json')
# df.to_csv('turn_farm_with_family_info.csv')
# print(df.head())

# df = pd.read_excel('turn_farm_2019.xlsx')
# df.to_json('turn_farm_2019.json', orient='records')

df = pd.read_json('turn_farm_with_family_info.json')
df.to_excel('tfwf.xlsx')
