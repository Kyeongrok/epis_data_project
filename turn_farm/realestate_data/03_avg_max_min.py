import json
from libs.AddressManager import AddressManager
from statistics import mean

am = AddressManager()

def calc_3_m(li):
    if len(li) > 0:
         return [mean(li), max(li), min(li)]
    else:
         return [0,0,0]
d = {}
with open('real_estate_prices.json') as f:
    jo = json.loads(f.read())
    # addr_code별, land_title별로 평균 max min구하기
    # print(len(jo))
    for row in jo:
        if d.get(row['addr_code']) == None:
            d[row['addr_code']] = {}
        if d.get(row['addr_code']).get('lad_bef') == None:
            d[row['addr_code']]['lad_bef'] =  []
        if d.get(row['addr_code']).get('lad_ricfld') == None:
            d[row['addr_code']]['lad_ricfld'] = []
        if d.get(row['addr_code']).get('orchrd') == None:
            d[row['addr_code']]['orchrd'] = []

        if row['land_title'] == '전':
            d[row['addr_code']]['lad_bef'].append(float(row['price']))
        if row['land_title'] == '답':
            d[row['addr_code']]['lad_ricfld'].append(float(row['price']))
        if row['land_title'] == '과수원':
            d[row['addr_code']]['orchrd'].append(float(row['price']))

print(len(d.items()))
d_result = {}
for item in d.items():
    it = item[1]
    lad_bef = calc_3_m(it['lad_bef'])
    lad_ricfld = calc_3_m(it['lad_ricfld'])
    orchrd = calc_3_m(it['orchrd'])
    # print(item)

    d_result[item[0]] = {
    'LAD_BFE_AVRG_AMOUNT':lad_bef[0],
    'LAD_BFE_TOP_AMOUNT': lad_bef[1],
    'LAD_BFE_LWET_AMOUNT': lad_bef[2],
    'LAD_RICFLD_AVRG_AMOUNT': lad_ricfld[0],
    'LAD_RICFLD_TOP_AMOUNT': lad_ricfld[1],
    'LAD_RICFLD_LWET_AMOUNT': lad_ricfld[2],
    'ORCHRD_AVRG_AMOUNT': orchrd[0],
    'ORCHRD_TOP_AMOUNT': orchrd[1],
    'ORCHRD_LWET_AMOUNT': orchrd[2]}


am.export_list_to_json_file(d_result, 'addr_code_real_estate_prices.json')