import json
from collections import Counter

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

law_codes = json.loads(open('addr_codes.json').read())
dic = json.loads(open('tree_law_adm.json').read())
err_cnt = 0

def get_adm_code(law_code):
    try:
        f = law_code[:2]
        s = law_code[2:5]
        t = law_code[5:]
        adm_code = dic[f][s][t]
        return adm_code
    except Exception as e:
        print('error---', law_code)
        return None

lst = []
for i in range(len(law_codes)):
    law_code = law_codes[i]
    adm_code = get_adm_code(law_code)
    if adm_code == None:
        err_cnt += 1
    else:
        lst.append(law_code)
        # print(adm_code)

print('err cnt:', err_cnt)

cnt = Counter(lst)
print(cnt)
print(len(cnt.keys()))
