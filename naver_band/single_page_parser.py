from bs4 import BeautifulSoup

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


