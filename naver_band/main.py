from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver.exe', options=chrome_options)

url = 'https://band.us/band/75387828'

driver.get(url)


for i in range(10):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

open('bd1.html', 'w+', encoding='utf-8').write(driver.page_source)