import json
import pandas as pd

def append_culture_centers(before_filename, cult_cnt_filename, target_filename):
    # turn farm
    jo = json.loads(open(before_filename).read())

    # 문화시설 개수
    jo_culture_cnt = json.loads(open(cult_cnt_filename).read())

    res = []
    for r in jo:
        # print(jo_culture_cnt[str(r['add_code'])])
        r['CLTUR_AVG_CO'] = 0
        if jo_culture_cnt.get(str(r['add_code'])) !=  None:
            add_cd = str(r['add_code'])
            # print(jo_culture_cnt[str(r['add_code'])])
            jjjo = jo_culture_cnt[add_cd]
            # print(jjj
            r['CLTUR_AVG_CO'] = jjjo['number']
        else:
            print('else:', r['add_code'])
        res.append(r)

    print(len(jo))
    print(len(res))
    open(target_filename, 'w+').write(json.dumps(res))
    pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

append_culture_centers('tf_fm_acc.json', 'culture_center_library_etc/culture_etc_cnt.json', 'tf_fm_acc_cult.json')