import glob, json, os, time
from threading import Thread
from libs.AddressManager import AddressManager
from collections import Counter
am = AddressManager()

# 서울특별시면 지운다.
target_filenames = [f for f in glob.glob('./success/' + "*.json")]

target_keys = am.get_distinct_keys() # int

l = []
def reduce(filename, i = '0'):
    with open(filename) as f:
        jo = json.loads(f.read())
    common = jo['results']['common']
    # print(common)
    if common['totalCount'] != '0':
        # print(jo)
        law_cd = jo['results']['juso'][0]['admCd']
        adm_cd = am.convert_to_adm_code_from_law_code(law_cd)
        return adm_cd

for target_filename in target_filenames:
    l.append(reduce(target_filename))

cnt = Counter(l)
print(cnt)
am.export_to_index_json(am.counter_to_list(cnt), 'academy_cnt.json', key_name='id')

