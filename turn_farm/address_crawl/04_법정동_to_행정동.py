import json
import pandas as pd
from collections import Counter
from libs.AddressManager import AddressManager

def make_law_addr_tree(file_name):
    adm_law_codes = open(file_name).readlines()[1:]

    tre = {}
    for i in range(len(adm_law_codes)):
        spl = adm_law_codes[i].replace('\n','').split(',')
        # spl에서 2개 3개 나머지를 자른다.
        fst = spl[1][:2]
        snd = spl[1][2:5]
        trd = spl[1][5:]

        print(fst, snd, trd, type(fst))
        if tre.get(fst) == None:
            tre[fst] = {}
        if tre[fst].get(snd) == None:
            tre[fst][snd] = {}
        if tre[fst].get(snd).get(trd) == None:
            tre[fst][snd][trd] = spl[0]

    open('tree_law_adm.json', 'w+').write(json.dumps(tre))

# make_law_addr_tree('adm_code_law_code.csv')

law_codes = json.loads(open('culture_center_addr_codes.json').read())
err_cnt = 0

am = AddressManager()

#
lst = []
for i in range(len(law_codes)):
    law_code = law_codes[i]
    adm_code = am.get_adm_code(law_code)
    if adm_code == None:
        err_cnt += 1
    else:
        lst.append(law_code)
        # print(adm_code)

print('err cnt:', err_cnt)

# 동별 문화의집, 도서관, 박물관, 지방문화원 등
cnt = Counter(lst)
print(len(cnt.keys()))
print(cnt)


li = am.counter_to_list(cnt)

pd.DataFrame(li).to_excel('ddd.xlsx')