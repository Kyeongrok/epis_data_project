import json
from libs.AddressManager import AddressManager
am = AddressManager()
'''
대안_초등학교_여부
대안_초중고_여부
대안_초중_여부
대안_중학교_여부
대안_중고_여부
대안_고등학교_여부
ALTRV_ELESCH_AT
ALTRV_ELESCH_MSKUL_HGSCHL_AT
ALTRV_ELESCH_MSKUL_AT
ALTRV_MSKUL_AT
ALTRV_MSKUL_HGSCHL_AT
ALTRV_HGSCHL_AT
있으면 1이고 없으면 0이다
'''
def alter_school(before_filename, target_filename):
    alter_school_cnt = json.load(open('./alter_school/alter_school_cnt.json'))
    # print(alter_school_cnt['4272033000'])
    l = []
    with open(before_filename) as f:
        jl = json.loads(f.read())
        for r in jl:
            r['ALTRV_ELESCH_AT'] = 0
            r['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = 0
            r['ALTRV_ELESCH_MSKUL_AT'] = 0
            r['ALTRV_MSKUL_AT'] = 0
            r['ALTRV_MSKUL_HGSCHL_AT'] = 0
            r['ALTRV_HGSCHL_AT'] = 0
            add_cd = str(r['add_code'])
            if alter_school_cnt.get(add_cd) != None:
                cnt = alter_school_cnt[add_cd]
                r['ALTRV_ELESCH_AT'] = cnt['ALTRV_ELESCH_AT']
                r['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = cnt['ALTRV_ELESCH_MSKUL_HGSCHL_AT']
                r['ALTRV_ELESCH_MSKUL_AT'] = cnt['ALTRV_ELESCH_MSKUL_AT']
                r['ALTRV_MSKUL_AT'] = cnt['ALTRV_MSKUL_AT']
                r['ALTRV_MSKUL_HGSCHL_AT'] = cnt['ALTRV_MSKUL_HGSCHL_AT']
                r['ALTRV_HGSCHL_AT'] = cnt['ALTRV_HGSCHL_AT']
            l.append(r)


    open(target_filename, 'w+').write(json.dumps(l))
    am.save_list_to_excel(l, target_filename.split('.')[0] + '.xlsx')


alter_school('t_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent.json', 't_fm_acc_cult_cv_locfd_apc_instut_real_estate_rent_alter_school.json')