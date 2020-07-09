import time
from threading import Thread
from libs.jsonFileSaver import save as json_save

import requests

def parse(json1):
    data = json1['data']
    # data_id
    return data

def gogo(page_idx, results):
    url = 'https://data.mafra.go.kr/opendata/data/open/getDataListPage.do'
    data = requests.post(url, data={
        'cur_page':page_idx,
        'rows':10
    })
    res = parse(data.json())
    results[page_idx] = res
    print('thread {} finished'.format(page_idx))

total_pages = 106 + 1 # index는 0번부터 page는 1번부터
threads = [None] * total_pages

results = [None] * total_pages

# {'rn': 1, 'total_cnt': 1054,
# 'file_infos': None, 'regist_id': None,
# 'regist_nm': None, 'regist_dt': '2014.01.22',
# 'regist_date': None, 'updt_id': None, 'updt_nm': None,
# 'updt_dt': None, 'updt_date': None,
# 'data_id': '20141014000000000093',
# 'data_nm': '농산물 이력 추적 등록정보',
# 'dataset_nm': '농산물이력추적등록정보', 'dataset_dc': None,
# 'data_dc': '이력추적등록번호, 생산자명, 대표자명, 유효기간, 품목, 주소, 등록필지수, 재배면적, 생산계획량', 'cl_code': '2202', 'cl_full_nm': '식품안전 > 이력추적', 'cl_nm_new': None,
# 'grid_provd_ennc': 'Y', 'file_provd_ennc': 'Y',
# 'api_provd_ennc': 'Y', 'link_provd_ennc': 'N', 'raw_data_provd_ennc': 'Y', 'entity_id': 'TI_NAQS_FRMPRD_CHGHST', 'api_id': None, 'provd_instt_id': '201410120002',
# 'provd_instt_nm': '국립농산물품질관리원', 'jrsd_instt_code': None, 'jrsd_instt_nm': None, 'kwrd_one': None, 'kwrd_two': None, 'kwrd_three': None, 'job_charger_psitn': None, 'job_charger_nm': None, 'job_charger_tlphon_no': None, 'dataset_rm': None, 'lang': None, 'lang_nm': None, 'hold_stl_code': None, 'hold_stle_nm': None, 'updt_cycle_code': None, 'updt_cycle_nm': None, 'nxttrm_regist_prarnde': None, 'threeman_right_incls_ennc': None,
# 'ccl_code': None, 'ccl_nm': None, 'opn_year': None, 'realm_code': 'open',
# 'rdcnt': 971, 'data_rm': None, 'tot_cnt': 0, 'map_provd_ennc': 'Y', 'chart_provd_ennc': 'N'}

for i in range(1, total_pages):
    threads[i] = Thread(target=gogo, args=(i, results))
    threads[i].start()
    print('thread {} started'.format(i))

time.sleep(total_pages / 3)

cnt = 0
result_total = []
for result in results:
    cnt += 1
    print(cnt, end='')
    if result != None:
        print(len(result), result)
        result_total += result

print(cnt)
json_save(result_total, 'mafra_total_data.json')
