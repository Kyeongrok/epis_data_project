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

import json
from libs.AddressManager import AddressManager
am = AddressManager()

alter_schools = json.loads(open('../alter_school/alter_school_add_code.json').read())
print(alter_schools)
d = {}
for r in alter_schools:
    print(r)
    add_cd = str(r['add_code'])
    if d.get(add_cd) == None:
        d[add_cd] = {}
        d[add_cd]['ALTRV_ELESCH_AT'] = 0
        d[add_cd]['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = 0
        d[add_cd]['ALTRV_ELESCH_MSKUL_AT'] = 0
        d[add_cd]['ALTRV_MSKUL_AT'] = 0
        d[add_cd]['ALTRV_MSKUL_HGSCHL_AT'] = 0
        d[add_cd]['ALTRV_HGSCHL_AT'] = 0

    if r['초'] == 1 and r['중'] == 1 and r['고'] == 1:
        d[add_cd]['ALTRV_ELESCH_MSKUL_HGSCHL_AT'] = 1
        print('-')
    elif r['초'] == 1 and r['중'] == 1:
        d[add_cd]['ALTRV_ELESCH_MSKUL_AT'] = 1
        print('--')
    elif r['중'] == 1 and r['고'] == 1:
        d[add_cd]['ALTRV_MSKUL_HGSCHL_AT'] = 1
        print('--')
    elif r['초'] == 1:
        d[add_cd]['ALTRV_ELESCH_AT'] = 1
    elif r['중'] == 1:
        d[add_cd]['ALTRV_MSKUL_AT'] = 1
    elif r['고'] == 1:
        d[add_cd]['ALTRV_ELESCH_AT'] = 1
print(d)
open('alter_school_cnt.json', 'w+', encoding='utf-8').write(json.dumps(d))

