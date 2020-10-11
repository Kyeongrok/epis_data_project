from libs.AddressManager import AddressManager
import pandas as pd
import json
from libs.address_finder import call_api
am = AddressManager()

li = json.loads(open('alter_school.json', encoding='utf-8').read())

result = []
for row in li:
    add_code = am.get_add_code(1, row['시도'], row['시군구'], row['읍면동'])
    if add_code == '':
        addr = '{} {} {}'.format(row['시도'], row['시군구'], row['읍면동'])
        res = call_api(addr)
        # print(res['results'])
        if res != '':
            law_cd = res['results']['juso'][0]['admCd']
            adm_cd = am.convert_to_adm_code_from_law_code(law_cd)
            print('law_cd:{}, adm_cd:{}'.format(law_cd, adm_cd))
            add_code = adm_cd
        else:
            print(addr)
    row['add_code'] = add_code
    result.append(row)

am.export_list_to_json_file(result, 'alter_school_add_code.json')
am.save_list_to_excel(result, 'alter_school_add_code.xlsx')
