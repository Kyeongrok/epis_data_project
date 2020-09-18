import sqlite3 as db
import pandas as pd
import json

con = db.connect('./road_name.db')



#  and 시군구 = "{}"
query = 'select distinct 시도, 시군구, 법정동코드, 도로명 from t_road_name'.format('서울특별시', '강남구', '개포로28길')
df = pd.read_sql(query, con = con)

# 시도 시군구
dic = {}
for idx, row in df.iterrows():
    if dic.get(row['시도']) == None:
        print(row['시도'])
        dic[row['시도']] = {}
    if dic[row['시도']].get(row['시군구']) == None:
        dic[row['시도']][row['시군구']] = {}
    if dic[row['시도']].get(row['시군구']).get(row['도로명']) == None:
        dic[row['시도']][row['시군구']][row['도로명']] = row['법정동코드']
    # print(idx)

open('road_nm_addr_code.json', 'w+').write(json.dumps(dic))