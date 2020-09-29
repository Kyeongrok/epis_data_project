from bs4 import BeautifulSoup

bsobj = BeautifulSoup(open('bank_addr_dev.html').read(), 'html.parser')
ol = bsobj.find_all('div', {'class':'search_list'}).find('ol')
list1s = ol.find_all('div', {'id':'list1'})
