# 학원 붙이기
import json
from libs.AddressManager import AddressManager

# load academy cnt
d_academy_cnt = json.load(open('./academy_cnt/academy_cnt.json'))

l = []
with open('t_fm_2019_acc_cult_cv_locfd_apc.json') as f:
    jl = json.loads(f.read())
    for r in jl:
        add_cd = str(r['add_code'])
        if d_academy_cnt.get(add_cd) !=  None:
            print(add_cd)
            academy_cnt = d_academy_cnt[add_cd]['number']
        else:
            academy_cnt = 0

        r['INSTUT_CO'] = academy_cnt
        l.append(r)

open('t_fm_2019_acc_cult_cv_locfd_apc_instut.json', 'w+').write(json.dumps(l))
am = AddressManager()
am.save_list_to_excel(l, 't_fm_2019_acc_cult_cv_locfd_apc_instut.xlsx')
