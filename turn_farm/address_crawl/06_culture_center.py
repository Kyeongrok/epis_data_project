import time

from libs.address_finder import call_api
from threading import Thread

def run(i, line, file):
    adm_cd = ''
    spl = line.replace('\n', '').split(',')
    if len(spl) > 4 and spl[5] == '':
        print('spl5:', spl[5])
        jo = call_api(spl[4])
        common = jo['results']['common']
        if len(spl) > 4 and spl[5] == '' and common['errorCode'] == '0' and common['totalCount'] != '0' :
            try:
                print(jo['results'])
                adm_cd = jo['results']['juso'][0]['admCd']
                print(line, adm_cd)
            except Exception as e:
                print(line, e)
    file.write('{},{},{}\n'.format(i, line.replace('\n', ''), str(adm_cd)))



lines = open('2019전국문화기반시설.csv', encoding='cp949').readlines()
file = open('result.csv', 'w+', encoding='cp949')
for i in range(0,len(lines)):
    print(i)
    line = lines[i]
    Thread(target=run, args=(i, line, file)).start()
    time.sleep(0.01)

# file = open('result2.csv', 'w+', encoding='cp949')
# run(37, lines[37], file)
