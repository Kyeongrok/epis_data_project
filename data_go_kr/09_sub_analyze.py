import pandas as pd

df = pd.read_json('./data_go_kr_total_result.json', dtype={'관리부서 전화번호':'str'})
print(df.shape)
# print(df['관리부서 전화번호'])
# df.to_csv('data_go_kr_total_result.csv')
df.to_excel('data_go_kr_total_result.xlsx')