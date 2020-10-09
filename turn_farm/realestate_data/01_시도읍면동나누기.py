from libs.AddressManager import AddressManager
import csv, json
# file읽어서 0번 column을 시도 시군구 읍면동으로 나눈다

# 시군구 읍면동 중 여기에 포함되어 있는 데이터만 남긴다.
# 세종특별자치시는 시군구가 없다. 참고할 것

# 시군구 읍면동으로 addr_code를 찾는다.
am = AddressManager()

f_lst = am.get_file_list('./raw_data/*.csv')
target_dic = json.load(open('./target_addr.json'))

def run(filename):
    res = []
    with open(filename, newline='') as f:
        ll = csv.reader(f)
        for _ in range(14):
            next(ll)
        for l in ll:
            addr_spl = l[0].split(' ')
            # 세종특별자치시 는 1번이 빈칸이다.
            if addr_spl == '세종특별자치시':
                pass
            else :
                try:
                    if target_dic.get(addr_spl[0]) is None or target_dic.get(addr_spl[0]).get(addr_spl[1]) is None:
                        print(addr_spl)
                    elif target_dic.get(addr_spl[0]).get(addr_spl[1]).get(addr_spl[2]) is not None:
                        res.append(l)
                except Exception as e:
                    print(e, '-------------------')
    return res

res = []
for i in range(len(f_lst)):
    f_nm = f_lst[i]
    res += run(f_nm)

with open('eee.csv', 'w+', newline='', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerows(res)

