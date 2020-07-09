import pandas as pd
from libs.singleExcelSaver import save

df = pd.read_json('mafra_total_with_link.json', dtype={'data_id':'str'})
df = df[['data_id', 'data_nm','link_provd_ennc', 'file_provd_ennc', 'link']]
save(df, 'mafra_with_link.xlsx')


