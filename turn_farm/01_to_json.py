# aa



import pandas as pd
import numpy as np
import json
from libs.AddressManager import AddressManager

df = pd.read_csv('./turn_farm_fminf.csv', encoding='utf-8')
df.reset_index().to_json('./turn_farm_fminf.json', orient='records')
df.to_excel('./turn_farm_fminf.xlsx')
#
# df['toddler'] = df.apply(lambda x: calc_toddler(x[['p1.age', 'p2.age', 'p3.age', 'p4.age', 'p5.age', 'p6.age', 'p7.age', 'p8.age', 'p9.age', 'p10.age']], 0, 4), axis=1)
# print(df)

#toddler	kinder	elem	middle	high	parents	child	teenager age_c

# am = AddressManager()


