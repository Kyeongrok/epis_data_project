import re
from bs4 import BeautifulSoup


def get_title_from_result(result_list):
    title = ''
    try:
        title = result_list.find('li').find('span', {'class':'title'}).text
        title = re.sub('(\n|\t|\r)', '', title)
    except Exception as e:
        print('get_title', e)
    return title

def parse(string):
    bs = BeautifulSoup(string, 'html.parser')
    result_lists = bs.find_all('div', {'class':'result-list'})
    titles = [get_title_from_result(result_list) for result_list in result_lists]
    return titles
