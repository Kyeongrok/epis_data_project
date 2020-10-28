from libs.AddressManager import AddressManager
from statistics import mean
am = AddressManager()

def category(csv_filename):
    d = {}
    li = am.read_csv_file_into_list(csv_filename)
    print(len(li))
    for item in li[1:]:
        # print(item[5], item[7], item[8])
        if d.get(item[8]) == None:
            d[item[8]] = {'광역교통시설':[], '교육시설':[], '의료시설':[], '판매시설':[]}
        try:
            print(item[8], item[5], item[7])
            d[item[8]][item[5]].append(float(item[7].replace('>', '')))
        except Exception as e:
            d[item[8]][item[5]].append(0)
    return d

def level2(csv_file_name):
    d = {}
    li = am.read_csv_file_into_list(csv_file_name)
    for item in li[1:]: # item = ['34917', '3902062', '제주특별자치도', '서귀포시', '예래동', '의료시설', '공공의료시설', '6.32275315804041', '5013062000', '20060701', '']
        if d.get(item[8]) == None:
            d[item[8]] = {'초등학교': 0,'중학교': 0,'고등학교': 0,'공공의료시설': 0,'병·의원': 0,'종합병원': 0,
            '대규모점포': 0,'전통시장': 0,'버스터미널': 0,'철도역': 0,'공항':0, '광역교통시설':[], '교육시설':[], '의료시설':[], '판매시설':[]}
        d[item[8]][item[6]] = 0
        try:
            d[item[8]][item[6]] = float(item[7].replace('>', ''))
        except Exception as e:
            print('error:', e)

        try:
            print(item[8], item[5], item[7])
            d[item[8]][item[5]].append(float(item[7].replace('>', '')))
        except Exception as e:
            d[item[8]][item[5]].append(0)
    return d

# d = category('2018시설접근성_add_code.csv')
# am.export_list_to_json_file(d, '2018_infra_accessibility.json')
d2 = level2('2018시설접근성_add_code.csv')
print(d2)
am.export_list_to_json_file(d2, '2018_infra_accessibility_level2.json')

