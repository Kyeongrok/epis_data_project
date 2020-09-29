import json
from libs.AddressManager import AddressManager

# load apc cnt
d_apc_cnt = json.load(open('./apc_cnt/apc_cnt.json'))

# load local food cnt
d_local_food_cnt = json.load(open('./local_food_cnt/local_food_cnt.json'))

# DISTB_AVG_CO
l = []
with open('t_fm_2019_acc_cult_cv.json') as f:
    for r in json.loads(f.read()):
        add_cd = str(r['add_code'])

        if d_apc_cnt.get(add_cd) !=  None:
            apc_cnt = d_apc_cnt[add_cd]['number']
        else:
            apc_cnt = 0

        if d_local_food_cnt.get(add_cd) !=  None:
            local_food_cnt = d_local_food_cnt[add_cd]['number']
        else:
            local_food_cnt = 0

        cnt_avg = (apc_cnt + local_food_cnt) / 2
        r['DISTB_AVG_CO'] = cnt_avg
        l.append(r)

open('t_fm_2019_acc_cult_cv_locfd_apc.json', 'w+').write(json.dumps(l))

am = AddressManager()
am.save_list_to_excel(l, 't_fm_2019_acc_cult_cv_locfd_apc.xlsx')
