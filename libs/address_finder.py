import requests

def call_api(addr):
    key = 'U01TX0FVVEgyMDIwMDkxODAxMjA1MzExMDIwNTM='
    url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey={}&currentPage=1&countPerPage=10&keyword={}&resultType=json'.format(key,addr)
    jo = requests.get(url).json()
    if jo['results']['common']['totalCount'] == '0':
        print('addr:{} totalCount is 0'.format(addr))
        return ''
    return jo

