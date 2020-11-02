from elasticsearch import Elasticsearch, helpers
from datetime import datetime
from libs.FileManager import FileManager
fm = FileManager()

es = Elasticsearch()
def insertDocument(doc):
    es.index(index="product_list", doc_type="_doc", body=doc)

def insert_document_bulk(items, index_name):
    print('origin cnt:', len(items))
    docs = []
    for i in range(len(items)):
        doc = {
            "_index": index_name,
            "_id": i,
            "_source": items[i]
        }
        docs.append(doc)
    print('bulk insert started. docs cnt:', len(docs), datetime.now())
    rtn = helpers.bulk(es, docs)
    print('bulk insert completed.', rtn, datetime.now())

# fl = fm.get_file_list('./separated/*.json')
# jo = fm.json_from_json_file_nm('2019_farmer.json')
jo = fm.json_from_json_file_nm('../turn_farm/tf_elem_middle_museum_bank_culture_etc_avg_item.json')
# print(jo)
insert_document_bulk(jo, 't_fm_data_set')

