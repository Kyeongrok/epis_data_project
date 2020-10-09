# addr_code 만들기
# 전, 답, 과수원 뽑기
# 각 동네의 전, 답, 과수원 max min mean을 구한다.
import json, csv
from libs.AddressManager import AddressManager
am = AddressManager()

l = []
with open('eee.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = list(csv.reader(csvfile))
    # print(len(spamreader))
    for row in spamreader:
        if row[2] in ['전', '답', '과수원']:
            add_sep = row[0].split(' ')
            add_code = am.get_add_code(1, add_sep[0], add_sep[1], add_sep[2])

            # print(add_code, row)
            result = {'land_title':row[2], 'size':float(row[7]), 'price':float(row[8].replace(',', '')), 'addr_code':add_code}
            l.append(result)

print(len(l))
am.export_list_to_json_file(l, 'real_estate_prices.json')
