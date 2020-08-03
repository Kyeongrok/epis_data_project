import pandas as pd

df = pd.read_json('mafra_subpage_total.json', dtype={'data_id':'str'})
df.to_excel('mafra_subpage_total.xlsx')