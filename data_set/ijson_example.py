import ijson
import json
import simdjson
from libs.FileManager import FileManager

fm = FileManager()
path = 'C:/Users/ocean/OneDrive/바탕 화면/빅데이터셋 3종/*.json'
files = fm.get_file_list(path)

def get_jo(file_name):
    category = file_name.split('생명자원정보_')[1].split('_')[0]
    print(category, 'has been started')
    tot = []
    with open(file_name, encoding='utf-8') as f:
        doc = simdjson.loads(f.read())
        for l in doc:
            l['category'] = category
            tot.append(l)
    return tot


tot = []
for i in range(5, 11):
    jo = get_jo(files[i])
    tot += jo

with open('bds_bio_resources.json', 'w+', encoding='utf-8-sig') as f2:
    idx = 1
    for l in tot:
        l['idx'] = idx
        f2.write(json.dumps(l, ensure_ascii=False) + '\n')
        idx += 1