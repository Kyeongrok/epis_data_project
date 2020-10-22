import glob, json, os, time
from threading import Thread
from libs.AddressManager import AddressManager
am = AddressManager()

# 서울특별시면 지운다.
target_filenames = [f for f in glob.glob('./success/' + "*.json")]

target_keys = am.get_distinct_keys() # int


def reduce(filename, i = '0'):
    with open(filename) as f:
        jo = json.loads(f.read())
    common = jo['results']['common']
    # print(common)
    if common['totalCount'] != '0':
        # print(jo)
        law_cd = jo['results']['juso'][0]['admCd']
        adm_cd = am.convert_to_adm_code_from_law_code(law_cd)
        if int(adm_cd) not in target_keys or jo['results']['juso'][0]['siNm'] == '서울특별시':
        # for juso in jo['results']['juso']:
        #     if juso['siNm'] == '서울특별시':
            if os.path.exists(filename):
                os.remove(filename)
                print(filename, 'removed')

        # return jo['results']['juso'][0]['admCd']
print(target_keys)
for target_filename in target_filenames:
    reduce(target_filename)