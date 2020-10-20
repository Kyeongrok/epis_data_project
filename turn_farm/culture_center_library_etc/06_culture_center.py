import time, csv

from libs.address_finder import call_api
from threading import Thread
from libs.AddressManager import AddressManager

am = AddressManager()

def run(row):
    print(row)
    if row['adm_code'] != '':
        return row
    if row['law_code'] == None:
        row['law_code'] = ''

    if row['law_code'] != '':
        law_cd = str(int(row['law_code']))
        row['law_code'] = law_cd
        row['adm_code'] = am.convert_to_adm_code_from_law_code(law_cd)
        return row

    adm_cd = ''
    if row['law_code'] == '':
        jo = call_api(row['address'])
        if jo == '':
            # 없으면 앞에서 4개만 가지고 해본다.
            spl = row['address'].split(' ')
            # 도를 찾아서 붙이고 한번 더 call한다.
            jo = call_api('{} {} {} {}'.format(spl[0], spl[1], spl[2], spl[3]))
            print(jo)
            if jo == '':
                do = row['sido']
                addr = '{} {}'.format(do, row['address'])
                jo = call_api(addr)
                if jo == '':
                    jo = call_api('{} {} {}'.format(spl[0], spl[1], spl[2]))
                results = jo['results']
                law_cd = results['juso'][0]['admCd']
                adm_cd = am.convert_to_adm_code_from_law_code(law_cd)
            else:
                results = jo['results']
                law_cd = results['juso'][0]['admCd']
                adm_cd = am.convert_to_adm_code_from_law_code(law_cd)
        else:
            results = jo['results']
            law_cd = results['juso'][0]['admCd']
            adm_cd = am.convert_to_adm_code_from_law_code(law_cd)

        row['adm_code'] = adm_cd
    else:
        row['adm_code'] = am.convert_to_adm_code_from_law_code(row['law_code'])
    return row


# am.csv_to_json('./2019전국문화기반시설.csv', 'cp949')
# file = open('./result.csv', 'w+', encoding='cp949')

jo = am.json_from_json_file_nm('./2019전국문화기반시설2.json')
result = []
for j in jo:
    r = run(j)
    result.append(r)
am.export_list_to_json_file(result, '2019전국문화기반시설.json')
am.save_list_to_excel(result, '2019문화기반시설.xlsx')