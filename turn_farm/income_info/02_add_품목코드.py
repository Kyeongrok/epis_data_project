# 품종명을 key로 dic을 만들어보자
import pandas as pd
import json, csv
from libs.AddressManager import AddressManager

am = AddressManager()

d = {}
d2 = {}
d_old = {}
li = am.read_csv_file_into_list('농수축산물_신구표준품목목록_20150101.csv', encoding='cp949')

# ['93', '9361', '어분류', '936102', '새우껍질어분']
for l in li:
    if d.get(l[4]) == None:
        d[l[4]] = []
    d[l[4]].append(l)

print(len(d))
for l in li[2:]:
    if d2.get(l[2]) == None:
        d2[l[2]] = []
    d2[l[2]].append(l)

for l in li[2:]:
    if d_old.get(l[5]) == None:
        d_old[l[5]] = []
    d_old[l[5]].append(l)

am.export_list_to_json_file(d, 'prd_cd.json')
am.export_list_to_json_file(d2, 'prd_cd_2.json')
am.export_list_to_json_file(d_old, 'prd_cd_old.json')
