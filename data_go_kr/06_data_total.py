import pandas as pd

df = pd.read_json('./data_total2.json')

df.to_csv('./data_total2.csv')

