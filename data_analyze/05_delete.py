
from elasticsearch import Elasticsearch
es = Elasticsearch()
# es.delete(index='farmer_2019')

es.indices.delete('farmer_2019')

res = es.count(index='farmer_2019')
print(res)

