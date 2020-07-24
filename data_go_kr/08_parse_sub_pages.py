import requests, re, json
from bs4 import BeautifulSoup
from libs.patternMatcher import findMatchedTexts
from os import listdir
from os.path import isfile, join

def get_text(tr):
    tds = tr.find_all('td')
    result = {}
    for td in tds:
        res = get_text_single(td)
        result.update(res)
    return result

def get_text_single(td):
    div_td = td.find('div', {'class':'td'})
    div_th = td.find('div', {'class':'th'})
    return {div_th.text:re.sub("(\n|\t)","",div_td.text)}

def get_phone_no(script_obj):
    rrr = findMatchedTexts(str(script_obj), 'var.*"')[0]
    nnn = findMatchedTexts(rrr, '[0-9]+')[0]
    return nnn

def get_title(data_set_title_obj):
    return data_set_title_obj.find('div', {'class':'tit-area'}).find('p').text

def get_data_info(table_obj):
    trs = table_obj.find_all('tr')
    result = {}
    for tr in trs:
        len_td = len(tr.find_all('div', {'class':'td'}))
        if len_td == 1:
            result.update(get_text_single(tr))
        elif len_td == 2:
            result.update(get_text(tr))
        else:
            # print('----------')
            # print(tr)
            print('----error get_data_info ----', len_td)
    return result

def parse_data(string):
    bsobj = BeautifulSoup(string, features='html.parser')
    table = bsobj.find('table', {'class':'dataset-table'})
    table_info = get_data_info(table)
    table_info['title'] = get_title(bsobj.find('div', {'class':'data-set-title'}))
    return table_info


mypath = '/Users/kyeongrok/git/python/epis_data/data_go_kr/data_go_kr_0723/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

total_result = []
cnt = 0
for file_name in onlyfiles[:100]:
    string = open(mypath + file_name).read()
    spli = file_name.split('_')
    # print(file.read())
    # meta data를 추가 해주기도 한다. title, type
    try:
        result = parse_data(string)
        # print(result)
        print(cnt, file_name)
        result['file_name'] = file_name
        result['type'] = spli[2].replace('.html','')
        cnt+=1
        total_result.append(result)
    except Exception as e:
        print(cnt, file_name, e)

file = open('data_go_kr_total_result.json', 'w+')
file.write(json.dumps(total_result))

