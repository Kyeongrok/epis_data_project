import requests

req = requests.get('https://github.com/southkorea/southkorea-maps/blob/master/kostat/2013/json/skorea_municipalities_geo_simple.json')
print(req.content)
