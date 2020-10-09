import json
import pandas as pd

def append_cv_store_theater_etc(target_filename):
    # turn farm
    jo = json.loads(open('tf_fm_acc_cult.json').read())

    #
    jo_cv_inf_cnt = json.loads(open('./cv_infra/cv_inf_cnt_idx.json').read())

    # print(jo_cv_inf_cnt)
    res = []
    for r in jo:
        # print(jo_cv_inf_cnt[str(r['add_code'])])
        r['CNVNC_AVG_CO'] = 0

        if jo_cv_inf_cnt.get(str(r['add_code'])) !=  None:
            add_cd = str(r['add_code'])
            # print(jo_cv_inf_cnt[str(r['add_code'])])
            jjjo = jo_cv_inf_cnt[add_cd]
            # print(jjj
            r['CNVNC_AVG_CO'] = jjjo['number'] / 18
        else:
            print('else:', r['add_code'])
        res.append(r)

    print(len(jo))
    # print(res)
    print(len(res))
    open(target_filename, 'w+').write(json.dumps(res))
    df = pd.DataFrame(res)
    df.to_excel(target_filename.split('.')[0] + '.xlsx')

append_cv_store_theater_etc('t_fm_acc_cult_cv.json')