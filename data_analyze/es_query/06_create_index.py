
from elasticsearch import Elasticsearch, helpers
from datetime import datetime
from libs.FileManager import FileManager
es = Elasticsearch()

mappings =  {
    'mappings':{
        "properties": {
            'age': {'type': 'long'},
            'career': {'type': 'long'},
            'category_level_1': {'type': 'text',
                                 'fields': {'keyword': {'type': 'keyword',
                                                        'ignore_above': 256}}},
            'category_level_2': {'type': 'text',
                                 'fields': {'keyword': {'type': 'keyword',
                                                        'ignore_above': 256}}},
            'category_level_3': {'type': 'text',
                                 'fields': {'keyword': {'type': 'keyword',
                                                        'ignore_above': 256}}},
            'cltv_ara_s': {'type': 'float'},
            'code': {'type': 'long'},
            'eqpt_cltv_ara_s': {'type': 'float'},
            'farm_emd': {'type': 'keyword'},
            'farm_sido': {'type': 'keyword'},
            'farm_sigungu': {'type': 'keyword'},
            'farm_type': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
            'gender': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
            'live_emd': {'type': 'keyword'},
            'live_sido': {'type': 'keyword'},
            'live_sigungu': {'type': 'keyword'},
            'motivation': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}, 'oudor_cltv_ara_s': {'type': 'float'}, 'prd_code': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}, 'reg_year': {'type': 'long'}
        }
    }
}

idx_nm = 'farmer_2019'
es.indices.delete(idx_nm)
r = es.indices.create(
    index=idx_nm,
    body=mappings
)
print(r)

print(es.indices.get_mapping(idx_nm))

