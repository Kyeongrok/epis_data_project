import pandas as pd
from libs.singleExcelSaver import save
from libs.jsonFileSaver import save as json_save
pd.set_option('display.max_colwidth', None)
pd.set_option('max_columns', None)
pd.options.display.float_format = '{:.0f}'.format

df = pd.read_json('mafra_total_data.json', dtype={'data_id':'str'})
# df['data_id'].apply(lambda x: int(x))

df.to_csv(path_or_buf='mafra_total.csv')

print(df['data_id'])

df_filter = df[(df['link_provd_ennc'] == 'Y') | (df['file_provd_ennc'] == 'Y')]
print(len(df_filter))

# print(df_filter.count())

df_2 = df_filter[['data_nm','link_provd_ennc', 'file_provd_ennc', 'data_id']]
# print(df_2.head(20))
# json_save(df_2.to_json(orient='records'), 'link_file_data_id.json')
# open('link_file_data_id.json','w+').write(df_2.to_json(orient='records'))

