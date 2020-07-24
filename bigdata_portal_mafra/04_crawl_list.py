'''
sub page crawler
crawl의 url, parser, loop문에 parameter값에 dependency가 있음
'''
import json
import requests
from bs4 import BeautifulSoup
from libs.crawler import crawl as ccrr
from libs.jsonFileSaver import save as json_save


# jo = json.loads(open('link_file_data_id.json').read())
jo = json.loads(open('mafra_total_data.json').read())

# mafra_total_data.json

def crawl(data_id):
    url = 'https://data.mafra.go.kr/opendata/data/indexDataLink.do'
    data = requests.post(url, data={'data_id':data_id}, headers={
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '28',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'_ga=GA1.3.48222570.1590990531; _gid=GA1.3.2121562496.1594009267; JSESSIONID=8pe2yDy1x1l6ZXjEeI4jwWUehlaIUv5ZDUZBN8a7qcxTaU6AVpha5995Axql98Ck.portal01_servlet_engine1; _gat=1',
        'Host': 'data.mafra.go.kr',
        'Origin': 'https://data.mafra.go.kr',
        'Referer':'https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?filter_ty=L&data_id=20191022000000001384',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    })
    return data.content

def file_parse(string):
    bsobj = BeautifulSoup(string, "html.parser")
    try:
        link = bsobj.find('tbody').find('a')['href']
        return link
    except:
        return 'no link'

# 20191022000000001384
rows = []
for row in jo:
    # data_id = format(row['data_id'], '.0f')
    # print(row['data_nm'], data_id)
    # file인 것을 수집해야 한다
    if(row['file_provd_ennc'] == 'Y'):
        print(row['data_id'], row['link_provd_ennc'], row['file_provd_ennc'])
        # url = 'https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?filter_ty=L&data_id={}'.format(20191022000000001384)
        # string = ccrr(url)
        data_id = row['data_id']
        string = crawl(data_id)
        link = file_parse(string)
        row['link'] = link
        rows.append(row)

# print(rows)
json_save(rows, 'mafra_total_with_file.json')
