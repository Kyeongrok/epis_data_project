import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver.exe', options=chrome_options)

def crawl_post(band_id, post_id):
    target_path = '{}/html'.format(band_id)
    if not os.path.isdir(target_path):
        os.makedirs(target_path)
    filename = '{}/{}.html'.format(target_path, post_id)
    # 해당 파일 없으면
    if not os.path.isfile(filename):
        url = 'https://band.us/band/{}/post/{}'.format(band_id, post_id)
        driver.get(url)
        time.sleep(0.5)
        page_source = driver.page_source
        page_source_len = len(page_source)
        cnt_wait = 0
        while (page_source_len < 100000 or page_source_len == 91933) and cnt_wait < 3:
            time.sleep(1)
            page_source = driver.page_source
            page_source_len = len(page_source)
            cnt_wait += 1
            print(cnt_wait, len(page_source), url)
        print(url, len(page_source))
        file = open(filename, 'w+', encoding='utf-8')
        file.write(page_source)
        file.close()
    else:
        print('{} already exist'.format(filename))

# band id로 dir을 만들고 그 안에 page를 .html로 저장 한다

# 댓글 2개 case

band_infos = [
    {"band_id":7727806, "category": '딸기', 'from':197480765, 'to': 426020244}, # 2020시작:426019840
    {"band_id":49247132, "category":'참외', 'from':309123755, 'to':425436125},
    {"band_id":56517936, "category":'토마토', 'from':2807, 'to':3465}, # 2020시작:3217
    {"band_id":56530371, "category":'오리', 'from':2, 'to':3688}, # 2020시작 : 3120
    {"band_id":56609722, "category":'무', 'from':353, 'to':492},
    {"band_id":53029650, "category": '염소', 'from': 429301115, 'to': 429301860},
]
# 인삼, 염소, 딸기


def get_post_ids(filename):
    file = open(filename)
    string = file.read()
    ar = string.replace('{','').replace('}','').replace("'","").replace(' ', '').split(',')
    return sorted(set(ar))

for i in range(len(band_infos)):
    band_info = band_infos[i]
    post_ids = get_post_ids('{}/{}_post_ids.json'.format(band_info['band_id'], band_info['band_id']))
    total = len(post_ids)
    for ii in range(len(post_ids)):
        try:
            crawl_post(band_info['band_id'], post_ids[ii])
            print('{}/{} completed'.format(ii, total))
        except Exception as e:
            print(e)