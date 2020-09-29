from libs.crawler import crawl

url = 'https://www.juso.go.kr/support/AddressMainSearch.do?currentPage={}&countPerPage={}&&searchType=location_newaddr&searchKeyword=%EC%9D%80%ED%96%89&lang=&sortType=acc'.format(1, 10)

open('bank_addr_dev.html', 'w+').write(crawl(url))