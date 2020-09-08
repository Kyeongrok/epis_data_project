import os
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver.exe', options=chrome_options)

band_id = 49247132
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