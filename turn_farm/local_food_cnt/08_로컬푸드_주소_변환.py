import json
from libs.AddressManager import AddressManager
from collections import Counter

from libs.AddressManager import AddressManager

def count_addr_code(result_f_nm, to_file_nm):
    am = AddressManager()
    jl = json.loads(open(result_f_nm).read())

    su = jl['succeed']
    adm_cds = []
    for item in su.keys():
        ll = su[item]
        lawcd = ll['juso'][0]['admCd']
        admcd = am.get_adm_code(lawcd)
        adm_cds.append(admcd)

    cnt = Counter(adm_cds)
    am = AddressManager()
    li = am.counter_to_list(cnt)
    print(li)
    am.export_to_index_json(li, 'local_food_cnt.json')
    am.save_list_to_excel(li, to_file_nm)
    print(cnt)
    print(len(adm_cds))
    print(len(jl['fail_idx']))
    print(jl['fail_idx'])

count_addr_code('local_food_location.json', 'local_food_cnt.xlsx')
# count_addr_code('apc_location.json', 'apc_location_cnt.xlsx')



