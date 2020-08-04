from libs.crawler import crawl
from bs4 import BeautifulSoup
import urllib.parse as enc
import re, json, threading, time
from data_go_kr.find_same_name.parser import parse


def gogo(idx, name, results):
    url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword={}'.format(enc.quote(name))
    dd= crawl(url)
    # open('for_develop_parser.html', 'w+', encoding='utf-8').write(dd)
    # dd = open('for_develop_parser.html', encoding='utf-8').read()
    infos = [''] * 3
    try:
        infos = parse(dd)
    except Exception as e:
        print(name, idx, e)
    results[idx] = {'name':name, 'url':url, 'title1':infos[0]['title'], 'title2':infos[1]['title'], 'title3':infos[2]['title']
                    , 'link1': infos[0]['link'], 'link2': infos[1]['link'], 'link3': infos[2]['link']
                    }

names = open('name.txt', encoding='utf-8').readlines()
threads = [None] * len(names)
results = [None] * len(names)

cnt = 0
for i in range(len(names)):
    threading.Thread(target=gogo, args=(i, names[i].replace('\n', ''), results)).start()
    cnt += 1
    time.sleep(0.01)
    print(cnt)

time.sleep(30)
open('total_v2.json', 'w+').write(json.dumps(results))
