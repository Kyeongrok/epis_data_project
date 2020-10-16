import pandas as pd
import json
from statistics import mean

def append_infra_accessibility(before_turn_farm_filename, cnt_file_name, target_filename):
    jo = json.loads(open(before_turn_farm_filename).read())
    jo_infra = json.load(open(cnt_file_name, encoding='utf-8'))

    res = []
    for r in jo:
        r['ARPRT_ACCES_POSBLTY'] = 0
        r['BUS_TRMINL_ACCES_POSBLTY'] = 0
        r['TRAIN_STATN_ACCES_POSBLTY'] = 0
        r['ELESCH_ACCES_POSBLTY'] = 0
        r['MSKUL_ACCES_POSBLTY'] = 0
        r['HGSCHL_ACCES_POSBLTY'] = 0
        r['PUBLIC_MLFLT_ACCES_POSBLTY'] = 0
        r['GNRL_HSPTL_ACCES_POSBLTY'] = 0
        r['GNRLZ_HSPTL_ACCES_POSBLTY'] = 0
        r['LRSCL_STOR_ACCES_POSBLTY'] = 0
        r['TRDIT_MRKT_ACCES_POSBLTY'] = 0

        if jo_infra.get(str(r['add_code'])) != None:
            try:
                acc = jo_infra[str(r['add_code'])]
                r['ARPRT_ACCES_POSBLTY'] = acc['공항']
                r['BUS_TRMINL_ACCES_POSBLTY'] = acc['버스터미널']
                r['TRAIN_STATN_ACCES_POSBLTY'] = acc['철도역']
                r['ELESCH_ACCES_POSBLTY'] = acc['초등학교']
                r['MSKUL_ACCES_POSBLTY'] = acc['중학교']
                r['HGSCHL_ACCES_POSBLTY'] = acc['고등학교']
                r['PUBLIC_MLFLT_ACCES_POSBLTY'] = acc['공공의료시설']
                r['GNRL_HSPTL_ACCES_POSBLTY'] = acc['병·의원']
                r['GNRLZ_HSPTL_ACCES_POSBLTY'] = acc['종합병원']
                r['LRSCL_STOR_ACCES_POSBLTY'] = acc['대규모점포']
                r['TRDIT_MRKT_ACCES_POSBLTY'] = acc['전통시장']
                res.append(r)
            except Exception as e:
                print('error:', e, r)
        else:
            print(r['add_code'], '가 jo_acc에 없음')

    print(res[0])
    print('jo len:', len(jo))

    open(target_filename, 'w+').write(json.dumps(res))
    pd.DataFrame(res).to_excel(target_filename.split('.')[0] + '.xlsx')

append_infra_accessibility('t_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent_alter_school.json',
    'infra_accessibility/2017_infra_accessibility_level2.json',
                       'tf_elem_middle.json')