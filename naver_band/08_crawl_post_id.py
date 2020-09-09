import os
import shutil

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

def crawl_post_id(band_id):
    url = 'https://band.us/band/{}'.format(band_id)
    driver.get(url)

    path = os.getcwd()
    cnt = 0
    for i in range(400):
        cnt+=1
        for i in range(3):
            time.sleep(0.5)
            # 일단 band를 다 돌아서 id랑 time을 수집해서 몇번부터 몇번까지를 뽑아야 될 듯?
            # scroll할 때 마다 로딩을 하기 때문에 쭉 돌린다음에 수집하는게 안될 듯?
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        target_dir = '{}/{}/pages'.format(path, band_id)
        file_name = '{}/{}.html'.format(target_dir, "{:03d}".format(cnt))
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        file = open(file_name, 'w+', encoding='utf-8')
        file.write(driver.page_source)
        file.close()
        print('{} page saved'.format(file_name))

band_infos = [
    {"band_id":7727806, "category": '딸기', 'from':197480765, 'to': 426020244}, # 2020시작:426019840
    {"band_id":49247132, "category":'참외', 'from':309123755, 'to':425436125},
    {"band_id":53029650, "category": '염소', 'from': 429301115, 'to': 429301860},
    {"band_id":56517936, "category":'토마토', 'from':2807, 'to':3465}, # 2020시작:3217
    {"band_id":56530371, "category":'오리', 'from':2, 'to':3688}, # 2020시작 : 3120
    {"band_id":56609722, "category":'무', 'from':353, 'to':492},
]

for band_info in band_infos:
    crawl_post_id(band_info['band_id'])