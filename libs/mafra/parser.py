from bs4 import BeautifulSoup


def get_row(li):
    dt_a = li.find('dt').find('a')
    link = dt_a['href']
    title = dt_a.find('span', {'class':'title'}).text
    title = title.strip()

    dd = li.find('dd')
    sub_title = dd.text

    div_info_data = li.find('div', {'class':'info-data'})
    ps = div_info_data.find_all('p')
    modified_date = ps[0].find('span', {'class':'data'}).text
    count = ps[1].find('span', {'class':'data'}).text.strip()

    use_requests = ""
    try:
        use_requests = ps[2].find('span',{'class':'data'}).text
    except Exception as e:
        print(e)

    return {'title':title, 'sub_title':sub_title, 'link':link, 'modified_date':modified_date,
            'count':count, 'use_requests':use_requests}

def parse(string):
    '''
    param string
    return []
    '''

    bsObj = BeautifulSoup(string, 'html.parser')
    # print(bsObj)
    result_list_ul = bsObj.find('div', {'class':'result-list'}).find('ul')
    lis = result_list_ul.find_all('li')
    print(len(lis))
    return [get_row(li) for li in lis]
