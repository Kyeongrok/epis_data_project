from libs.crawler import crawl

auth_key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
url = 'http://apis.data.go.kr/B552895/openapi/service/OrgPriceJointMarketService/getJointMarketPriceList?ServiceKey={}&pageNo=1&numOfRows=10&delngDe=20150501&jmrktCd={}'.format(
    auth_key, '2')

res = crawl(url)
print(res)