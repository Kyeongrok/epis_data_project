import json
with open('bds_safe_restaurant_error.json', encoding='utf-8') as f:
    ls = f.readlines()
    for l in ls:
        print(json.loads(l))
