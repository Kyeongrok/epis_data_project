import pandas as pd
import requests, time
from threading import Thread

df = pd.read_json('/Users/kyeongrok/git/python/epis_data/data_go_kr/data_total2.json')
print(df.shape)
# /data/15057646/openapi.do
# /data/15045785/fileData.do
# /data/15017325/standard.do
# 위 3가지 /로 split해서 파일명 할 것
# link column사용 idx 2, 3 사용
# url = https://www.data.go.kr/data/15061784/openapi.do
threads = [None] * df.shape[0]

def crawl_and_save(idx, link):
    splt = link.split('/')
    url_prefix = 'https://www.data.go.kr'
    url = url_prefix + link
    print(url)
    page_str = requests.get(url).text
    # print(page_str)
    file = open('/Users/kyeongrok/git/python/epis_data/data_go_kr/data_go_kr_0723/{}_{}_{}.html'.format(str(idx).zfill(4), splt[2], splt[3].split('.')[0]), 'w+')
    file.write(str(page_str))
    file.close()
    print('{} success'.format(idx))

cnt = 0
for link in df['link']:
    cnt += 1
    print(link, cnt)
    try:
        Thread(target=crawl_and_save, args=(cnt, link)).start()
    except Exception as e:
        print('error=>', link, e)
    time.sleep(0.01)

time.sleep(60)

# crawl해서 id로 파일 저장
# 3034933_fileData, /data/15048199/fileData.do,
# /data/15048200/fileData.do, 15047233_fileData, 15050283_fileData,
# 3055325_fileData, 3076485_fileData, 0134_15056587_openapi.html
# 0060_15056587_openapi.html


