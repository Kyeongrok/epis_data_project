import json

jj = json.loads(open('result10000.json').read())

items = jj['response']['body']['items']['item']

print(len(items))

for item in items:
    # print(item)
    print(item['stdPrdlstNewNm'], item['stdMtcNewNm'], item['ledgNo'], item['delngDe'], item['cprMtcCode'])