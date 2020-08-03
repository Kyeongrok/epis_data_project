from libs.crawler import crawl
from bs4 import BeautifulSoup
import urllib.parse as enc
import re, json, threading, time


def get_title_from_result(result_list):
    title = ''
    try:
        title = result_list.find('li').find('span', {'class':'title'}).text
        title = re.sub('(\n|\t|\r)', '', title)
    except Exception as e:
        print('get_title', e)
    return title

def parse(string):
    bs = BeautifulSoup(string, 'html.parser')
    result_lists = bs.find_all('div', {'class':'result-list'})
    titles = [get_title_from_result(result_list) for result_list in result_lists]
    return titles

def gogo(idx, name, results):
    url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword={}'.format(enc.quote(name))
    dd= crawl(url)
    # open('for_develop_parser.html', 'w+', encoding='utf-8').write(dd)
    # dd = open('for_develop_parser.html', encoding='utf-8').read()
    titles = [''] * 3
    try:
        titles = parse(dd)
    except Exception as e:
        print(name, idx, e)
    results[idx] = {'name':name, 'url':url, 'title1':titles[0], 'title2':titles[1], 'title3':titles[2]}

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
open('total.json', 'w+').write(json.dumps(results))
