import pandas as pd

df = pd.read_csv('turn_farm_with_family_info_2.csv')
df.to_json('turn_farm_2019_2.json', orient='records')

