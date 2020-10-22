import json
from collections import Counter
from libs.AddressManager import AddressManager

am = AddressManager()

# id만 뽑아서 counter로 개수 센다

l = []
with open('bank_list.json') as f:
    jo = json.loads(f.read())
    for j in jo:
        l.append(j['add_code'])

print(l)

cnt = Counter(l)
print(cnt)
li = am.counter_to_list(cnt)
am.export_to_index_json(li, 'bank_cnt.json', 'id')
