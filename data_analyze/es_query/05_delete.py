
from elasticsearch import Elasticsearch
es = Elasticsearch()

# es.indices.delete('farmer_2019')

res = es.count(index='farmer_2019')
print(res)

