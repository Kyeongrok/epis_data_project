from libs.AddressManager import AddressManager
import pandas as pd
am = AddressManager()

keys = am.get_distinct_keys(target_fields=['code'], target_column='code')

# 각 연도별 json을 연다.
# keys에 포함 되어있는 것만 l에 넣고 저장한다.
def run():
    l = []
    already_exisist = []
    for i in range(9, 4, -1):
        filename = 'farmers/farmer_201{}_idx.json'.format(i)
        jo = am.json_from_json_file_nm(filename)
        for k, v in jo.items():
            # print(k, v, type(k))
            if int(k) in keys and int(k) not in already_exisist:
                print(filename, k)
                v['연번'] = k
                l.append(v)
                already_exisist.append(int(k))
    return l
l = run()
am.export_to_index_json(l, 'farmer_item_code_name_idx.json', '연번', ['연번'])

