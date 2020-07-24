'''
data.go.kr의
도매시장 가격 api
OrgPriceAuctionService 모니터링용
'''
import requests, time
import xmltodict, json, xmljson
from datetime import datetime
auth_key = 'PO0%2FZnoDAPq13aXDpR7e7JfTu6xSTlZNATSkgJ0s5sRoRdNcPzlvQgTIJ4ZiiqRwW5EP1Pu2FzefeObZWvZp7A%3D%3D'
prd_lst_code = 1001
num_of_rows = 3000
delngDe = '20200703'
url = 'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList' \
      '?ServiceKey={}&pageNo=1&numOfRows={}&delngDe={}&' \
      'prdlstCd={}'.format(auth_key, num_of_rows, delngDe, prd_lst_code)
print(datetime.now())
data = requests.get(url)

# print(data.text)
o = xmltodict.parse(data.text)
jsonnn = json.dumps(o)
open('result{}_{}.json'.format(delngDe, prd_lst_code), 'w+').write(jsonnn)
jj = json.loads(jsonnn)
print(jj)
items = jj['response']['body']['items']['item']
print(len(items))
print(datetime.now())
