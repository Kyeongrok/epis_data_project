from elasticsearch import Elasticsearch
from libs.ESHelper import ESHelper
esh = ESHelper()
es = Elasticsearch()

# result = esh.searchAPI('farmer_2019')
# hits = result['hits']['hits']
# print(len(hits))
# for item in hits:
#     print(item)

res = es.count(index='farmer_2019')
print(res)
print(es.indices.get_mapping('farmer_2019'))
# farm_sido, live_sido
q = \
{
    'size':0,
    'aggs':{
        'dd':{
            'cardinality':{'field':'live_sido'}
        }
    }
}
r = es.search(index='farmer_2019', body=q)
print(r)
print(r['aggregations'])

esh.print_each_line(r['hits']['hits'])
