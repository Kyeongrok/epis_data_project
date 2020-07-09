import pandas as pd
from libs.singleExcelSaver import save
pd.set_option('display.max_colwidth', None)
pd.set_option('max_columns', None)
pd.options.display.float_format = '{:.0f}'.format

df = pd.read_json('mafra_total_data.json')

print(df.shape)
print(df.head(5))
print(df.count())

df = df[['data_id', 'rdcnt', 'regist_dt', 'data_nm', 'dataset_nm', 'grid_provd_ennc', 'file_provd_ennc',
'api_provd_ennc', 'link_provd_ennc', 'chart_provd_ennc', 'provd_instt_nm']]

# save(df, 'mafra.xlsx')

gr = df.groupby('provd_instt_nm')
print(gr['data_id'].count())

