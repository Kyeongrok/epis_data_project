import pandas as pd
path ='C:/Users/ocean/Desktop/total_mafra_in_datagokr_complete_v2.xlsx'

def get_data_go_kr_id(row):
    result = ''
    if isinstance(row, str):
        try:
            splitted = row.split('/')
            # print(splitted[4:])
            result = splitted[4]
        except Exception as e:
            print('error', row)
    return result


# df = pd.read_csv(path, encoding='utf-8', dtype={'id':'str'})
df = pd.read_excel(path, dtype={'id':'str'})
# df = df.head(1)
# print(df[['id', 'site']])

df['data_go_kr_id'] = df['site'].apply(lambda x: get_data_go_kr_id(x))

df.to_excel('dddd.xlsx')


