import glob, os, platform, time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

def run(fr_city, to_addr, owner_age):
    url = 'http://localhost:8080/bdp/svc/retnFmlg/retnFmlgInfo.do'
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[1]/input').send_keys(fr_city)
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[1]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="addrModal"]/div/div[2]/div/div/div[1]/input[2]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="setAddrBtn"]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[2]/div/label[1]/span').click()
    driver.find_element_by_xpath('//*[@id="selfDiv"]/div[3]/input').send_keys(owner_age)

    # 2.
    driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div[3]/div[1]/div[1]/div/label[1]/span').click()
    driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div[3]/div[1]/div[3]/input').send_keys(32)

    # 3.
    driver.find_element_by_xpath('//*[@id="hopeAreaDiv"]/div/input').send_keys(to_addr)
    driver.find_element_by_xpath('//*[@id="hopeAreaDiv"]/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="addrModal"]/div/div[2]/div/div/div[1]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="setAddrBtn"]').click()

    # 4.
    driver.find_element_by_xpath('//*[@id="hopeCtvtDiv"]/div/input').send_keys('토마토')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="showResultBtn"]').click()

run('서울특별시 서초구','충청남도 홍성군', owner_age=49)