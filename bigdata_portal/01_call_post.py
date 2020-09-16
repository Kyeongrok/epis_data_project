import requests

url = 'http://localhost:8080/bdp/svc/retnFmlg/retnFmlgDetail.do'
url = 'http://localhost:8080/bdp/svc/retnFmlg/retnFmlgDetail.json'
print(requests.post(url).content)