

import ijson
import json
import simdjson
from libs.FileManager import FileManager
fm = FileManager()
# with open('bds_bio_resources.json', encoding='utf-8') as f:
#     doc = simdjson.loads(f.read())
#     print('fin')


path = 'C:/Users/ocean/Desktop/빅데이터셋 3종/*.json'

fnms = fm.get_file_list(path)
print(fnms[11])



N = 30
with open(fnms[11], encoding='utf-8') as myfile:
    head = [next(myfile) for x in range(N)]
print(len(head))
for l in head:
    print(l)
