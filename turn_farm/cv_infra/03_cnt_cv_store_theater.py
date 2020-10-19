import csv, json
from libs.AddressManager import AddressManager
am = AddressManager()

# ['4369', '휴게음식점', '07_24_05_P', '3000000', '3000000-104-1982-09443', '19820326', '', '03', '폐업', '02', '폐업', '19990317', '', '', '', '  0207640549', '', '110126', '서울특별시 종로구 종로6가 239-30번지 ', '', '', '사랑', '20010929000000', 'I', '2018-08-31 23:59:59.0', '다방', '200421.084607111    ', '452228.70909565     ', '다방', '0', '3', '기타', '갑', '상수도전용', '', '', '', '', '', '', '', '', 'N', '134.44', '', '', '']

# 주소 편의점 개수, 극장 개수
def run():
    d = {}

    target_keys = am.get_distinct_keys()
    print(target_keys)
    err_cnt = 0
    with open('07_24_05_P.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # 10이 영업 폐업 28업태구분명
            addr_spl = row[18].split(' ')
            if len(addr_spl) < 2 or addr_spl[0] == '서울특별시' or row[10] == '폐업': #
                err_cnt += 1
                continue
            add_code = am.get_add_code('a', addr_spl[0],addr_spl[1],addr_spl[2])
            if add_code == '' or int(add_code) not in target_keys:
                continue
            if d.get(add_code) == None:
                d[add_code] = {'cv_cnt':0, 'theater_cnt':0}
            if row[28] == '편의점':
                d[add_code]['cv_cnt'] += 1
            if row[28] == '극장':
                d[add_code]['theater_cnt'] += 1
    #     print('err_cnt:', err_cnt)
    return d

d = run()
print(d)
am.export_list_to_json_file(d, 'cv_store_bank_cnt.json')
