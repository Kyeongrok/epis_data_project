from elasticsearch import Elasticsearch
es = Elasticsearch()

# 요청 쿼리문 작성
resp = es.search(
    index = 'farmer_2019',
    body =
{
    "size": 100,
    "_source": {
        "includes": [ "code", 'live_sido', 'farm_sido' ],
    },
    "query": {
        "match_all": {}
    },
    'aggs':{
        'langs':{
            'terms':{'field':'live_sido'}
        }
    },
    # "collapse" : {
    #    "field" : "code"
    # },
    "sort": [
        {
          "code": {
            "order": "asc"
          }
        }
      ]
},
    # scroll = '3s'
)

# old_scroll_id = resp['_scroll_id']
# print(old_scroll_id)
for r in resp['hits']['hits']:
    print(r['_source'])

print(resp['aggregations'])

# while len(resp['hits']['hits']):
#     resp = es.scroll(
#         scroll_id=old_scroll_id,
#         scroll = '1s'
#     )
#     old_scroll_id = resp['_scroll_id']
#
#     for doc in resp['hits']['hits']:
#         print(doc)
