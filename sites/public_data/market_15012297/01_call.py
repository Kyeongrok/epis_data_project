import requests, time
import xmltodict, json, xmljson
from datetime import datetime

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
      print('start at:{}'.format(datetime.now()))
      data = requests.get(url)
      return data.text

def get_rows(prd_lst_code, delngDe):
      text = crawl(prd_lst_code, delngDe)
      o = xmltodict.parse(text)
      jsonnn = json.dumps(o)
      jj = json.loads(jsonnn)

      items = []
      if jj['response']['body']['items'] != None:
            items = jj['response']['body']['items']['item']
      print(delngDe, prd_lst_code, len(items))
      print('end at:{}'.format(datetime.now()))

      open('result{}_{}.json'.format(delngDe, ), 'w+').write(jsonnn)


prd_lst_code = 804
delngDe = '20200713'

# {'status':'', items:[]}

