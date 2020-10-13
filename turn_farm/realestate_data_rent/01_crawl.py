import requests, json
from bs4 import BeautifulSoup
from libs.AddressManager import AddressManager
am = AddressManager()
targets = [
{'do':'경기도', 'do_cd':41,'last_page':4},
{'do':'강원도', 'do_cd':42, 'last_page':4},
{'do':'충청북도', 'do_cd':43, 'last_page':18},
{'do':'충청남도', 'do_cd':44, 'last_page':21},
{'do':'전라북도', 'do_cd':45, 'last_page':8},
{'do':'전라남도', 'do_cd':46,'last_page':18},
{'do':'경상북도', 'do_cd':47, 'last_page':19},
{'do':'경상남도', 'do_cd':48, 'last_page':12}
]

def get_a_row(tr):
    tds = tr.find_all('td')
    if len(tds) > 0:
        spl = tds[2]['onclick'].replace("javascript:fn_bgChange(this,'infoDetail');fn_mapView(",'').replace(");", "").split(',')
        addr = spl[1].replace("'",'')
        spl_addr = addr.split(' ')
        law_code = spl[2].replace("'",'')
        return {'category':tds[1].text, 'land_title':tds[5].text, 'price':tds[3].text.replace(",", ""), 'size':tds[4].text.replace(',',''),
                'addr_code':law_code, 'addr':addr, 'sido':spl_addr[0], 'sigungu':spl_addr[1], 'emd':spl_addr[2]}

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    search_list = bsobj.find('table', {'class':'search_list'})
    trs = search_list.find_all('tr')
    li = [get_a_row(tr) for tr in trs[1:]]
    return li

def run(area_id, page_index):
    url = 'https://www.alimi.or.kr/dataview/a/selectAgriculturalMarketing.do'
    data = requests.post(url, data={'pageIndex': page_index,
                                    'areaCityId':'','sortSubject':'',
                                    'sortDescend':'ASC',
                                    'areaId':area_id,
                                    'cityId':'','dong':'','BIZCL_NM':''}, headers={})

    with open('crawl_result/{}_{}.json'.format(area_id, page_index), 'w+', encoding='utf-8')as f:
        f.write(json.dumps(parse(data.text)))

# with open('crawl_result/41_1.html', encoding='utf-8') as f:
#     parse(f.read())

for target in targets:
    for i in range(1, target['last_page'] + 1):
        print(i)
        run(target['do_cd'], i)


