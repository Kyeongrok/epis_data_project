import requests, time
import xmltodict, json, xmljson
from datetime import datetime
from threading import Thread

'''
:param prd_lst_code: 
:return: 
'''

def crawl(prd_lst_code, delngDe):
      auth_key = 'PO0%2FZnoDAPq13aXDpR7e7JfTu6xSTlZNATSkgJ0s5sRoRdNcPzlvQgTIJ4ZiiqRwW5EP1Pu2FzefeObZWvZp7A%3D%3D'
      num_of_rows = 3000
      url = 'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList' \
            '?ServiceKey={}&pageNo=1&numOfRows={}&delngDe={}&' \
            'prdlstCd={}'.format(auth_key, num_of_rows, delngDe, prd_lst_code)
      print('{} start at:{}'.format(prd_lst_code, datetime.now()))
      data = requests.get(url)
      return data.text

def get_rows(idx, results, prd_lst_code, delngDe):
      text = crawl(prd_lst_code, delngDe)
      o = xmltodict.parse(text)
      jsonnn = json.dumps(o)
      jj = json.loads(jsonnn)
      print(jj)
      items = []
      try:
            tmp = jj['response']['body']['items']
            print(tmp)
            if tmp != None:
                  items = tmp['item']
                  print(items, tmp)
            print('idx:{} end at:{}'.format(idx, datetime.now()), delngDe, prd_lst_code, len(items))
            results[idx] = items
      except Exception as e:
            print('prd_lst_code:{}'.format(prd_lst_code), e)
            print(jj)

prd_lst_code = 804
delngDe = '20200713'

# {'status':'', items:[]}
# code목록 불러오기 840 910193 46407

code_list = open('code_list.txt').readlines()
results = [None] * len(code_list)
threads = [None] * len(code_list)

for i in range(len(code_list))[110:200]:
      threads[i] = Thread(target=get_rows, args=(i, results, code_list[i], delngDe))
      threads[i].start()

time.sleep(30)

print(results)