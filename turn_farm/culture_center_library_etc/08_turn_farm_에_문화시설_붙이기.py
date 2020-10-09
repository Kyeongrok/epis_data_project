import json
import pandas as pd
df = pd.read_excel('동별_문화의집_도서관_지방문화원_etc.xlsx')
df = df.set_index('id')
df.to_json('culture_etc_cnt.json', orient='index')


