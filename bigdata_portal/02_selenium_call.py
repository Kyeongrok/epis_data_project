import glob, os, platform, time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

def run(url, fr_city, to_addr, crop, owner_age):
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[1]/input').send_keys(fr_city)
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[1]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="addrModal"]/div/div[2]/div/div/div[1]/input[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="setAddrBtn"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[2]/div/label[1]/span').click()
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[3]/input').send_keys(owner_age)

    # 2.동거가족 배우자
    driver.find_element_by_xpath('/html/body/div/section/div[2]/div[2]/div[1]/div[1]/div/label[1]/span').click()
    driver.find_element_by_xpath('/html/body/div/section/div[2]/div[2]/div[1]/div[3]/input').send_keys(32)

    # 3.
    driver.find_element_by_xpath('//*[@id="hopeAreaDiv"]/div/input').send_keys(to_addr)
    driver.find_element_by_xpath('//*[@id="hopeAreaDiv"]/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="addrModal"]/div/div[2]/div/div/div[1]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="setAddrBtn"]').click()

    # 4.
    driver.find_element_by_xpath('//*[@id="hopeCtvtDiv"]/div/input').send_keys(crop)
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="showResultBtn"]').click()


url = 'http://localhost:8080/ReturnFarm'
url = 'https://bigdata.agrion.kr/bdp/svc/retnFmlg/retnFmlgInfo.do'
url = 'http://localhost:8080/ReturnFarm'
url = 'https://bigdata.agrion.kr/ReturnFarm'
run(url, '도움3로','조치원', '딸기', owner_age=34)