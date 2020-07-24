import pandas as pd
import json, requests, time
from threading import Thread

jo = json.loads(open('mafra_total_data.json').read())

def crawl_and_save(idx, data_id):
    url = 'https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?data_id={}'.format(data_id)
    page_str = requests.get(url).text
    file = open('/Users/kyeongrok/git/python/epis_data/bigdata_portal_mafra/mafra_subpages/{}_{}.html'.format(str(idx).zfill(4), data_id), 'w+')
    file.write(str(page_str))
    file.close()
    print('{} success'.format(idx))

cnt = 0
for row in jo:
    Thread(target=crawl_and_save, args=(cnt, row['data_id'])).start()
    cnt +=1
    time.sleep(0.1)

time.sleep(40)