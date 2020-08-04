import re
from bs4 import BeautifulSoup


def get_title_from_result(result_list):

    # print(result_list)

    title = ''
    try:
        title = result_list.find('li').find('span', {'class':'title'}).text
        title = re.sub('(\n|\t|\r)', '', title)
    except Exception as e:
        print('get_title', e)

    link = ''
    try:
        dt_a = result_list.find('dt').find('a')
        link = 'https://www.data.go.kr'+dt_a['href']
    except Exception as e:
        print('get_link', e)

    return {'title':title, 'link':link}

def parse(string):
    bs = BeautifulSoup(string, 'html.parser')
    result_lists = bs.find_all('div', {'class':'result-list'})
    infos = [get_title_from_result(result_list) for result_list in result_lists]
    return infos

dd = open('for_develop_parser.html', encoding='utf-8').read()

print(parse(dd))
