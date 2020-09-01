from bs4 import BeautifulSoup

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    DPostLayoutViews = bsobj.find_all('div', {'class':'cCard gContentCardShadow'})
    print(len(DPostLayoutViews))
    pass


string = open('bd1.html', encoding='utf-8').read()


parse(string)
