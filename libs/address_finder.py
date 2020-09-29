import requests

def call_api(addr):
    key = 'U01TX0FVVEgyMDIwMDkxODAxMjA1MzExMDIwNTM='
    url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do?confmKey={}&currentPage=1&countPerPage=10&keyword={}&resultType=json'.format(key,addr)
    return requests.get(url).json()

