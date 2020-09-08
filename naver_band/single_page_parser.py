from bs4 import BeautifulSoup

# 게시물의 id를 받아오기 위해 만듬
# range로 하면 중간에 빠진 번호가 너무 많고 범위도 넓어서 불가능

def get_row(DPostLayoutView):
    postListInfoWrap = DPostLayoutView.find('div', {'class':'postListInfoWrap'})
    if postListInfoWrap != None:
        post_url = postListInfoWrap.find('a')['href']
        post_id = post_url.split('post/')[1]
        return post_id

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    DPostLayoutViews = bsobj.find_all('div', {'data-viewname':'DPostLayoutView'})

    rows = []
    for DPostLayoutView in DPostLayoutViews:
        row = get_row(DPostLayoutView)
        if row != None:
            rows.append(row)
    return rows


