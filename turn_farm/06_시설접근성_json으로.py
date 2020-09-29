import pandas as pd

df_acc = pd.read_excel('2017시설접근성_add_code.xlsx', sheet_name='pivot')
df_acc = df_acc.set_index('add_code')
df_acc.to_json('2017시설접근성_add_code.json', orient='index')


