from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver.exe', options=chrome_options)

url = 'https://band.us/band/56609722'

driver.get(url)


for i in range(2):
    time.sleep(1)
    # 일단 band를 다 돌아서 id랑 time을 수집해서 몇번부터 몇번까지를 뽑아야 될 듯?
    # scroll할 때 마다 로딩을 하기 때문에 쭉 돌린다음에 수집하는게 안될 듯?
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

open('bd1.html', 'w+', encoding='utf-8').write(driver.page_source)