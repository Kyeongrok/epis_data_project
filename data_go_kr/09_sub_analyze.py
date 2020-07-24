import pandas as pd

df = pd.read_json('./data_go_kr_total_result.json')
print(df.shape)
df.to_csv('data_go_kr_total_result.csv')