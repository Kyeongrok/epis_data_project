from libs.AddressManager import AddressManager
import pandas as pd
am = AddressManager()

keys = am.get_distinct_keys(target_fields=['code'], target_column='code')

def run():
    l = []
    with open('farmers/2015년 경영주.txt') as f:
        for line in f.readlines()[1:]:
            spl = line.split('	')
            if int(spl[0]) in keys:
                print(line)
                l.append(line)
    print(l)
    am.export_list_to_json_file(l, '2015_fm.json')


dd = [383876,340555,360912,342086,362078,380953,347654,380284,371087,372712,368308,389082,349925,385194,346627,360261,378125,387176,366662,371124,368009,361539,360874,362013,373921,385273,364988,351939,354194,359065,363290,364165,350124,
366814,346963,368228,363779,353097,387794,380011,361446]
jo = am.json_from_json_file_nm('2015_fm.json')
ee = []
d = {}
for line in jo:
    spl = line.replace('\n', '').split('	')
    if int(spl[0]) in dd:
        ee.append({spl[0], spl[13], spl[16]})
        if d.get(spl[0]) == None:
            d[spl[0]] = {'품목코드':spl[13], '소분류':spl[16]}

am.export_list_to_json_file(d, 'farmers/farmer_2015_idx.json')
print(len(dd), len(ee))
print(d)
print(len(d.keys()))