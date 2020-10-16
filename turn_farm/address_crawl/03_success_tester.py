import json
from collections import Counter
with open('../academy_cnt/success.json') as f:
    su_ids = json.loads(f.read())
    print(len(su_ids))

with open('../academy_cnt/academy_addr_codes.json') as f:
    cnt = Counter()
    ll = json.loads(f.read())
    for itm in ll:
        cnt[itm] += 1
    print(len(cnt))
    print(cnt)
