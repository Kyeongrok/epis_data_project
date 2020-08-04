import pandas as pd
import json

string = open('total_v2.json').read()
jj = json.loads(string)

pure = []
for j in jj:
    if j != None:
        pure.append(j)

df = pd.DataFrame(pure)
df.to_excel('total_mafra_in_datagokr_v2.xlsx')

