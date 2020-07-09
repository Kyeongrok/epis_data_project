import time
from threading import Thread
import requests
from libs.mafra.parser import parse
from libs.jsonFileSaver import save as json_save

# dType : TOTAL, API, FILE, STD
def crawl(url, page_idx):
    '''
    param url, page_idx
    return data from url
    '''
    data = requests.post(url, data ={
            'currentPage': page_idx,
            'dType': 'FILE',
            'brm': '농축수산',
            'url': '/tcs/dss/selectConditionSearch.do',
            'size': 10
        })
    return data

def multi_page_crawl(page_idx, results):
    url = 'https://www.data.go.kr/tcs/dss/selectConditionSearch.do'
    data = crawl(url, page_idx)

    results[page_idx] = parse(data.content)

    print("{} finished".format(page_idx))

def thread_run(fn, total_pages):
    '''
    :param fn: fn은 crawl + parse로 result를 []로 주는 fn
    :param total_pages:
    :return:
    '''
    total_pages += 1
    threads = [None] * total_pages
    results = [None] * total_pages

    for i in range(1, total_pages):
        threads[i] = Thread(target=fn, args=(i, results))
        threads[i].start()
        print('thread {} started'.format(i))

    time.sleep(total_pages / 2)

    list = []
    for i in range(1, len(results)):
        list+= results[i]
    return list

results = thread_run(multi_page_crawl, 173)

json_save(results, 'data_file.json')

