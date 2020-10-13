import json
from libs.AddressManager import AddressManager

def append_apc_cult_cv(target_filename):
    # load apc cnt
    d_apc_cnt = json.load(open('./apc_cnt/apc_cnt.json'))

    # load local food cnt
    d_local_food_cnt = json.load(open('./local_food_cnt/local_food_cnt.json'))

    # DISTB_AVG_CO
    l = []
    with open('t_fm_acc_cult_cv.json') as f:
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

            # 2가지 항목이기 때문에 /2해준 값을 붙인다.
            cnt_avg = (apc_cnt + local_food_cnt) / 2
            r['DISTB_AVG_CO'] = cnt_avg
            r['APC'] = apc_cnt
            l.append(r)

    open(target_filename, 'w+').write(json.dumps(l))
    am = AddressManager()
    am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')

append_apc_cult_cv('t_fm_acc_cult_cv_locfd_apc.json')