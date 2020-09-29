import json
import os

import pandas as pd
from libs.address_finder import call_api
from libs.AddressManager import AddressManager

am = AddressManager()

def collect(addrs, result_f_nm):
    jl = {}
    res = {}
    fail_idx = set()

    if not os.path.isfile(result_f_nm):
        open(result_f_nm, 'w+').close()

    with open(result_f_nm) as f:
        try:
            jl = json.loads(f.read())
            fail_idx = set(jl['fail_idx'])
        except Exception as e:
            print(e, 'during file open')

    for i in range(len(addrs)):
        addr = addrs[i]
        try:
            jo = call_api(addr)
            results = jo['results']
            if len(results['juso']) == 0:
                # 도를 찾아서 붙이고 한번 더 call한다.
                do = am.find_do(addr.split(' ')[0])
                addr = '{} {}'.format(do, addr)
                print('retry:', addr)
                if do != '':
                    results = call_api(addr)['results']
            if results['common']['totalCount'] != '0':
                res[i] = results
            else:
                fail_idx.add(i)

            print(i, addr, results)
            # res.add(i)
        except Exception as e:
            fail_idx.add(i)
            print(e, addr)

    # file에 index를 만든다.
    # index가 없거나 index에 값이 예상값이 아니면 다시 try한다.

    content = {'fail_idx':list(fail_idx), 'succeed':res}
    open(result_f_nm, 'w+').write(json.dumps(content))

# df = pd.read_excel('C:/Users/ocean/Desktop/(200916) 데이터 수집 목록/10. APC 현황/농산물산지유통센터(APC) 데이터_20200915.xls')
# addrs = list(df['소재지'])
# collect(addrs, 'apc_location.json')

collect(list(pd.read_excel('C:/Users/ocean/Desktop/(200916) 데이터 수집 목록/9. 로컬푸드매장 현황/전국 로컬푸드직매장 운영현황(469개소).xlsx')['주소']), 'local_food_location.json')