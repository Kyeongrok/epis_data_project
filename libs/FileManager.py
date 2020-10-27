import glob
import json
import os
from datetime import datetime

class FileManager():
    def __init__(self):
        pass

    def json_from_json_file_nm(self, filename):
        with open(filename, encoding='utf-8') as f:
            return json.loads(f.read())

    '''
    params
    file_location : './separated/*.json'
    '''
    def get_file_list(self, file_location):
        file_names = glob.glob(file_location)
        print(len(file_names))
        return file_names

    '''
    params
    from_filename:str
    file_cnt:int default = 10
    target_path default = './separated/'
    '''
    def separate_files(self, from_filename, file_cnt=10, target_path='./separated/'):
        print('started at:', datetime.now())
        with open(from_filename) as f:
            jo = json.loads(f.read())
            records_per_file = len(jo) // file_cnt
            print('total:', len(jo))
            for i in range(file_cnt):
                if i == file_cnt - 1:
                    oo = jo[i * records_per_file: len(jo)]
                else:
                    oo = jo[i * records_per_file: i * records_per_file + records_per_file]
                # target_path가 없으면 만든다.
                if not os.path.isdir(target_path):
                    os.makedirs(target_path)

                # oo를 저장한다.

                with open('{}{:02d}_{}'.format(target_path, i, from_filename), 'w+') as f:
                    f.write(json.dumps(oo))
        print('finished at:', datetime.now())
