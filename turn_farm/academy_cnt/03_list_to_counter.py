import json
from collections import Counter
from libs.AddressManager import AddressManager

am = AddressManager()

cnt = Counter(json.loads(open('academy_addr_codes.json', encoding='utf-8').read()))
print(cnt)
li = am.counter_to_list(cnt)
# print(li)
#
am.save_list_to_excel(li, 'academy_cnt.xlsx')
am.export_to_index_json(li, 'academy_cnt.json')



