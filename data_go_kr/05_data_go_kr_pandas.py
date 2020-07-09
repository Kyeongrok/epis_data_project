import pandas as pd
from libs.jsonFileSaver import save as json_save
from libs.singleExcelSaver import save as excel_save
import json

# df = pd.read_json('./data_api.json')
#
# print(df.shape)
# excel_save(df, 'data_api.xlsx')

# json에 type을 추가 할 것

# data_api.json, data_file

# results = []
# results += json.loads(open('data_api2.json').read())
# results += json.loads(open('data_file2.json').read())
# results += json.loads(open('data_std2.json').read())
#
# json_save(results, 'data_total.json')
# file_provd_ennc, api_provd_ennc, std_provd_ennc

# api_jo = json.loads(open('data_std.json').read())
#
# for row in api_jo[0]:
#     row['api_provd_ennc'] = 'F'
#     row['file_provd_ennc'] = 'F'
#     row['std_provd_ennc'] = 'Y'
#
json_o = json.loads(open('data_total2.json').read())

# extract data_id from total
nl = []
# for row in json_o:
#     data_id = row['link'].replace('/data/','')\
#         .replace('/standard.do', '') \
#         .replace('/fileData.do', '')\
#         .replace('/openapi.do', '')
#
#     row['data_id'] = data_id
#     nl.append(row)

# print(nl[0]['data_id'])

# json_save(nl, 'data_total2.json')
print(json_o[0])





