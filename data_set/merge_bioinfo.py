import json
from libs.FileManager import FileManager
from datetime import datetime

fm = FileManager()
path = 'C:/Users/ocean/OneDrive/바탕 화면/빅데이터셋 3종/*.json'
path = 'D:/*.json'
path = 'C:/Users/ocean/Desktop/빅데이터셋 3종/*.json'

files = fm.get_file_list(path)

# for fnm in files:
#     print(fnm)

# for i in range(len(files)):
#     with open(files[i], encoding='utf-8') as f:
#         jo = json.loads(f.read())
#         print(files[i], len(jo))

with open(files[9], encoding='utf-8') as f:
    print(datetime.now())
    f.readlines()
    print(datetime.now())
    # jo = json.loads(f.read())
    # print(files[4], len(jo))

