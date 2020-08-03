import re, json
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

def parse_tb1(table):
    trs = table.find('tbody').find_all('tr')
    row = {}
    for tr in trs:
        ths = tr.find_all('th')
        tds = tr.find_all('td')
        for i in range(len(ths)):
            column_name = ths[i].text
            value = re.sub("(\n|\t|\\xa0)", "", tds[i].text)
            if column_name == '업무담당자':
                # 담당부서, 부서 전화번호
                spl = value.split('/')
                value = spl[1]
                row['담당부서'] = spl[0]
                row['담당부서_전화'] = spl[2]
            row[column_name] = value
    return row

def parse_mafra_subpage(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    title = bsobj.find('p',{'class':'tit'}).find('strong').text
    tb1 = bsobj.find('div', {'class':'tbl-type02 mt10'}).find('table')
    tb2 = bsobj.find('div', {'class':'tbl-type02 mt30'}).find('table')
    result = {'title':title}
    result.update(parse_tb1(tb1))
    result.update(parse_tb1(tb2))
    return result

mypath = '/Users/kyeongrok/git/python/epis_data/bigdata_portal_mafra/mafra_subpages/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

total_result = []
for file_name in onlyfiles:
    file = open(mypath + file_name)
    row = parse_mafra_subpage(file.read())
    data_id = file_name.split('_')[1].replace('.html', '')
    row.update({'data_id':data_id, 'data_url':'https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?data_id={}'.format(data_id)})
    total_result.append(row)
    file.close()
    print(file_name)

file = open('./mafra_subpage_total.json', 'w+')
file.write(json.dumps(total_result))