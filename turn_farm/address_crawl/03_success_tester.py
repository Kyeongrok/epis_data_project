import json
from collections import Counter
with open('success.json') as f:
    su_ids = json.loads(f.read())
    print(len(su_ids))

with open('addr_codes.json') as f:
    cnt = Counter()
    ll = json.loads(f.read())
    for itm in ll:
        cnt[itm] += 1
    print(len(cnt))
    print(cnt)
