import os, sys
from glob import glob
import requests, json, time, datetime
from threading import Thread


def call_api(addr):
    key = 'U01TX0FVVEgyMDIwMDkxODAxMjA1MzExMDIwNTM='
    url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey={}&currentPage=1&countPerPage=10&keyword={}&resultType=json'.format(key,addr)
    return requests.get(url).json()


# 어떤 error가 몇번 index에서 났는지를 실행 후에 알아야 한다.
def run(idx, addr):
    try:
        # print('try:{}'.format(i))
        jo = call_api(addr)
        if jo['results']['common']['errorCode'] == '0':
            target_path = './success/'
            if not os.path.isdir(target_path):
                os.makedirs(target_path)
            filename = './success/{}.json'.format(idx)
            with open(filename, 'w+') as f:
                f.write(json.dumps(jo))
            print('{} success'.format(idx))
        elif jo['results']['common']['totalCount'] == '0':
            print('totalCount is 0', addr)
        else:
            print('fail:',idx)
    except Exception as e:
        print('error:', idx, e)

# 없는 번호 뽑아내기
addrs = open('../address/학원주소.txt', encoding='utf-8').readlines()
target_ids = [int(f.replace('./success\\', '').replace('.json', '')) for f in glob('./success/' + "*.json")]

# success
filenames = glob('./success/*.json')
finished = set()
with open('success.json') as f:
    ll = f.read()
    finished = set([int(row) for row in json.loads(ll)])

# total - success
target = set([i for i in range(len(addrs))]) - finished - set(target_ids)

print('total:{} target_ids:{}, finished:{} target:{}'.format(len(addrs), len(target_ids), len(finished), len(target)))
if input('will you go? 0:exit other:go') == '0':
    sys.exit(1)

for i in target:
    # print(len(target))
    addr = addrs[i]
    Thread(target=run, args=(i, addr)).start()
    time.sleep(0.0000001)

