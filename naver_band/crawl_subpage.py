
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver.exe', options=chrome_options)

def crawl_post(band_id, post_id):
    url = 'https://band.us/band/{}/post/{}'.format(band_id, post_id)
    print(url)
    driver.get(url)
    time.sleep(2)
    file = open('{}/html/{}.html'.format(band_id, post_id), 'w+', encoding='utf-8')
    file.write(driver.page_source)
    file.close()

# band id로 dir을 만들고 그 안에 page를 .html로 저장 한다

# 댓글 2개 case
ddd = [{"band_id":56517936, "category":'토마토', 'from':3174, 'to':3465},
    {"band_id":56530371, "category":'오리', 'from':3109, 'to':3688},
    {"band_id":56609722, "category":'무', 'from':400, 'to':492},
    {"band_id":49247132, "category":'참외', 'from':425435833, 'to':425436125},
    {"band_id": 53029650, "category": '염소', 'from': 429301115, 'to': 429301860},
   {"band_id": 7727806, "category": '딸기', 'from': 426019823, 'to': 426020244},
       ]

# 인삼, 염소, 딸기

for i in range(5,6):
    band_info = ddd[i]
    for post_id in range(band_info['from'], band_info['to'] + 1):
        try:
            crawl_post(band_info['band_id'], post_id)
        except Exception as e:
            print(e)