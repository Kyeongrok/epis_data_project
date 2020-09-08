from bs4 import BeautifulSoup

def get_row(DPostLayoutView):
    # print(DPostLayoutView)
    postListInfoWrap = DPostLayoutView.find('div', {'class':'postListInfoWrap'})
    #post올린 시각
    ttime = postListInfoWrap.find('time').text
    year = ttime.split(', ')[1]

    postAuthorRegion = DPostLayoutView.find('div', {'class':'_postAuthorRegion'})
    # print(postAuthorRegion)

    profileInner_img_alt = postAuthorRegion.find('span', {'class':'profileInner'}).find('img')['alt']

    post_url = DPostLayoutView.find('div', {'class':'postListInfoWrap'}).find('a')['href']
    post_id = post_url.split('post/')[1]

    # count인가? 잉?
    count = DPostLayoutView.find('div', {'class':'postCountRight'}).find('span', {'class':'count'}).text

    post_body = ''

    # 훔... id를 수집해야될듯 ㅋㅋ

    return {'time':ttime, 'user_nick':profileInner_img_alt, 'post_id':post_id, 'post_url':post_url, 'post_year':year, 'count':count}

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    DPostLayoutViews = bsobj.find('div', {'class':'cCard gContentCardShadow'})
    print(len(DPostLayoutViews))

    rows = []
    for DPostLayoutView in DPostLayoutViews:
        try:
            row = get_row(DPostLayoutView)
            rows.append(row)
        except Exception as e:
            print('---- nothing ----')
    return rows


string = open('49247132/html/425435833.html', encoding='utf-8').read()
print(parse(string))
