from elasticsearch import Elasticsearch
from libs.ESHelper import ESHelper
import json
esh = ESHelper()
es = Elasticsearch()

# result = esh.searchAPI('farmer_2019')
# hits = result['hits']['hits']
# print(len(hits))
# for item in hits:
#     print(item)

res = es.count(index='ddd2')
print(res)
print(json.dumps(es.indices.get_mapping('ddd2')))
# farm_sido, live_sido
q = \
{
    'size':100,
    # "query":{
    #     "bool":{
    #       "must": [
    #         { "match": { "sido":"" }}
    #       ]
    #     }
    # }
}
r = es.search(index='ddd2', body=q)
print(r)

esh.print_each_line(r['hits']['hits'])
