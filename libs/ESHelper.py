from elasticsearch import Elasticsearch, helpers

class ESHelper():
    def __init__(self, es=Elasticsearch()):
        self.es = es


    def searchAPI(self, index_name, size=10):
        # ===============
        # 데이터 조회 []
        # ===============
        es = Elasticsearch()
        index = index_name
        body = \
            {
                'size':size,
                'query':{
                    'match_all':{}
                }
            }
        res = es.search(index=index, body=body)
        return res

    def print_each_line(self, hits):
        for hit in hits:
            print(hit)


