#  시도	시군구	사업자명	소재지	연락처	품목1	품목2	품목3

# 소재지에서 읍면을 뽑아 adm_code를 뽑고 개수를 센다.
import csv, json
from libs.AddressManager import AddressManager
from collections import  Counter

filename = 'C:/Users/ocean/Desktop/(200916) 데이터 수집 목록/10. APC 현황/농산물산지유통센터(APC) 데이터_20200915.csv'
sido_eup_men_amd_cd_dic = json.loads(open('../address/eup_men_dong_addr_cd.json').read())

am = AddressManager()
road_nm_addr_cd_dic = am.road_nm_adm_cd_dic

total = 0
cnt = 0
addr_cds = []
with open(filename, newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        total += 1
        add_spl = row[3].split(' ')
        if len(add_spl) >= 3:
            try:
                cnt += 1
                print(add_spl[0], add_spl[1], add_spl[2])
                if sido_eup_men_amd_cd_dic.get(add_spl[0]).get(add_spl[1]).get(add_spl[2]) != None:
                    adm_addr_cd = sido_eup_men_amd_cd_dic[add_spl[0]][add_spl[1]][add_spl[2]]
                    addr_cds.append(adm_addr_cd)
                else:
                    law_addr_cd = road_nm_addr_cd_dic[add_spl[0]][add_spl[1]][add_spl[2]]
                    addr_cds.append(law_addr_cd)
            except Exception as e:
                print(e)

print(cnt, total, len(addr_cds))
cnt = Counter(addr_cds)
l_cnt = am.counter_to_list(cnt)
am.export_to_index_json(l_cnt, 'apc_cnt.json')
am.save_list_to_excel(l_cnt, 'apc_cnt.xlsx')