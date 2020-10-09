import pandas as pd
import json
from statistics import mean

def append_infra_accessibility(before_turn_farm_filename, target_filename):
    jo = json.loads(open(before_turn_farm_filename).read())
    jo_acc = json.load(open('infra_accessibility/2017_infra_accessibility.json', encoding='utf-8'))

    # {'광역교통시설': [], '교육시설': [], '의료시설': [], '판매시설': []}
    res = []
    for r in jo:
        r['TRNSPORT_AVG_ACCES_POSBLTY'] = 0
        r['EDC_AVG_ACCES_POSBLTY'] = 0
        r['HSPTL_AVG_ACCES_POSBLTY'] = 0
        r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = 0

        if jo_acc.get(str(r['add_code'])) != None:
            try:
                acc = jo_acc[str(r['add_code'])]
                r['TRNSPORT_AVG_ACCES_POSBLTY'] = mean(acc['광역교통시설'])
                r['EDC_AVG_ACCES_POSBLTY'] = mean(acc['교육시설'])
                r['HSPTL_AVG_ACCES_POSBLTY'] = mean(acc['의료시설'])
                r['CNVNC_MRKT_AVG_ACCES_POSBLTY'] = mean(acc['판매시설'])
                res.append(r)
            except Exception as e:
                print(e, r)
        else:
            print(r['add_code'], '가 jo_acc에 없음')

    print(res[0])
    print('jo len:', len(jo))

    open(target_filename, 'w+').write(json.dumps(res))
    pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

append_infra_accessibility('turn_farm_fminf.json','tf_fm_acc.json')